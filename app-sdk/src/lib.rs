#![cfg_attr(feature = "target_vanadium_ledger", no_main, no_std)]

// Ensure exactly one target feature is enabled
#[cfg(all(feature = "target_native", feature = "target_vanadium_ledger"))]
compile_error!(
    "Features `target_native` and `target_vanadium_ledger` are mutually exclusive. Enable only one."
);

#[cfg(not(any(feature = "target_native", feature = "target_vanadium_ledger")))]
compile_error!("Either `target_native` or `target_vanadium_ledger` feature must be enabled.");

extern crate alloc;

#[cfg(feature = "target_native")]
extern crate lazy_static;

use alloc::vec::Vec;

pub mod app;
pub mod bignum;
pub mod comm;
pub mod curve;
pub mod executor;
pub mod hash;
pub mod rand;
pub mod rsa;
pub mod slip21;
pub mod storage;
pub mod ux;

pub use app::{App, AppBuilder, IsReady, TaskHandle};
pub use vanadium_macros::handler;

#[cfg(not(feature = "raw_ecalls"))]
mod ecalls;

/// The raw ECALLs, bypassing the SDK's wrappers. Only meant for testing the ECALLs themselves.
#[cfg(feature = "raw_ecalls")]
pub mod ecalls;

#[cfg(feature = "target_vanadium_ledger")]
mod ecalls_riscv;

#[cfg(feature = "target_native")]
mod ecalls_native;

#[allow(unused_assignments)]
mod ux_generated {
    include!(concat!(env!("OUT_DIR"), "/ux_generated.rs"));
}

use core::alloc::{GlobalAlloc, Layout};
use core::sync::atomic::{AtomicUsize, Ordering};

#[cfg(feature = "target_vanadium_ledger")]
use embedded_alloc::Heap;

#[cfg(feature = "target_vanadium_ledger")]
include!(concat!(env!("OUT_DIR"), "/heap_config.rs"));

#[cfg(feature = "target_vanadium_ledger")]
static mut HEAP_MEM: [u8; VAPP_HEAP_SIZE] = [0; VAPP_HEAP_SIZE];

static CURRENT_HEAP_BYTES: AtomicUsize = AtomicUsize::new(0);
static PEAK_HEAP_BYTES: AtomicUsize = AtomicUsize::new(0);

#[inline]
fn record_alloc(size: usize) {
    let prev = CURRENT_HEAP_BYTES.fetch_add(size, Ordering::Relaxed);
    let cur = prev.saturating_add(size);
    let mut peak = PEAK_HEAP_BYTES.load(Ordering::Relaxed);
    while cur > peak {
        match PEAK_HEAP_BYTES.compare_exchange_weak(
            peak,
            cur,
            Ordering::Relaxed,
            Ordering::Relaxed,
        ) {
            Ok(_) => break,
            Err(actual) => peak = actual,
        }
    }
}

#[inline]
fn record_dealloc(size: usize) {
    let mut cur = CURRENT_HEAP_BYTES.load(Ordering::Relaxed);
    loop {
        let next = cur.saturating_sub(size);
        match CURRENT_HEAP_BYTES.compare_exchange_weak(
            cur,
            next,
            Ordering::Relaxed,
            Ordering::Relaxed,
        ) {
            Ok(_) => break,
            Err(actual) => cur = actual,
        }
    }
}

struct TrackingHeap {
    #[cfg(feature = "target_vanadium_ledger")]
    inner: Heap,
    #[cfg(feature = "target_native")]
    inner: std::alloc::System,
}

impl TrackingHeap {
    #[cfg(feature = "target_vanadium_ledger")]
    const fn new() -> Self {
        Self {
            inner: Heap::empty(),
        }
    }

    #[cfg(feature = "target_native")]
    const fn new() -> Self {
        Self {
            inner: std::alloc::System,
        }
    }
}

unsafe impl GlobalAlloc for TrackingHeap {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        let ptr = unsafe { self.inner.alloc(layout) };
        if !ptr.is_null() {
            record_alloc(layout.size());
        }
        ptr
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        unsafe { self.inner.dealloc(ptr, layout) };
        record_dealloc(layout.size());
    }

    unsafe fn alloc_zeroed(&self, layout: Layout) -> *mut u8 {
        let ptr = unsafe { self.inner.alloc_zeroed(layout) };
        if !ptr.is_null() {
            record_alloc(layout.size());
        }
        ptr
    }

    unsafe fn realloc(&self, ptr: *mut u8, layout: Layout, new_size: usize) -> *mut u8 {
        let new_ptr = unsafe { self.inner.realloc(ptr, layout, new_size) };
        if !new_ptr.is_null() {
            if new_size >= layout.size() {
                record_alloc(new_size - layout.size());
            } else {
                record_dealloc(layout.size() - new_size);
            }
        }
        new_ptr
    }
}

#[global_allocator]
static HEAP: TrackingHeap = TrackingHeap::new();

#[inline]
pub fn current_heap_bytes() -> usize {
    CURRENT_HEAP_BYTES.load(Ordering::Relaxed)
}

#[inline]
pub fn peak_heap_bytes() -> usize {
    PEAK_HEAP_BYTES.load(Ordering::Relaxed)
}

#[inline]
pub fn reset_peak_heap_bytes() -> usize {
    let cur = CURRENT_HEAP_BYTES.load(Ordering::Relaxed);
    PEAK_HEAP_BYTES.swap(cur, Ordering::Relaxed)
}

#[cfg(feature = "target_vanadium_ledger")]
fn init_heap() {
    unsafe {
        #[allow(static_mut_refs)]
        HEAP.inner.init(HEAP_MEM.as_mut_ptr() as usize, VAPP_HEAP_SIZE);
    }
}

// embedded-alloc requires an implementation of critical_section::Impl
use critical_section::RawRestoreState;

struct CriticalSection;
critical_section::set_impl!(CriticalSection);

/// Default empty implementation as we don't have concurrency.
unsafe impl critical_section::Impl for CriticalSection {
    unsafe fn acquire() -> RawRestoreState {}
    unsafe fn release(_restore_state: RawRestoreState) {}
}

// Allocator initialization for target_vanadium_ledger targets
#[cfg(feature = "target_vanadium_ledger")]
#[unsafe(no_mangle)]
pub extern "C" fn rust_init_heap() {
    init_heap();
}

pub fn fatal(msg: &str) -> ! {
    // SAFETY: msg.as_ptr() is valid for msg.len() bytes and contains valid UTF-8.
    unsafe { ecalls::fatal(msg.as_ptr(), msg.len()) };
}

pub fn exit(status: i32) -> ! {
    ecalls::exit(status);
}

#[cfg(feature = "target_vanadium_ledger")]
#[panic_handler]
fn my_panic(_info: &core::panic::PanicInfo) -> ! {
    fatal("V-App panic"); // does not return; avoids heap allocation & core::fmt bloat
}

pub fn xrecv(size: usize) -> Vec<u8> {
    // We allocate a buffer with the requested size, but we don't initialize its content.
    // xrecv guarantees that recv_size have been overwritten with the received data, and we
    // do not access any further data.
    let mut buffer = Vec::with_capacity(size);
    unsafe {
        buffer.set_len(size);
    }

    let recv_size =
        // SAFETY: buffer is a Vec with at least `size` bytes of writable capacity (set_len above).
        unsafe { ecalls::xrecv(buffer.as_mut_ptr(), buffer.len()) };
    buffer[0..recv_size].to_vec()
}

pub fn xrecv_to(buf: &mut [u8]) -> usize {
    // SAFETY: buf is a valid mutable slice reference.
    unsafe { ecalls::xrecv(buf.as_mut_ptr(), buf.len()) }
}

pub fn xsend(buffer: &[u8]) {
    // SAFETY: buffer is a valid slice reference.
    unsafe { ecalls::xsend(buffer.as_ptr(), buffer.len() as usize) }
}

pub fn get_device_property(property_id: u32) -> u32 {
    ecalls::get_device_property(property_id)
}

pub fn print(message: *const u8, size: usize) {
    // SAFETY: the caller is responsible for ensuring message is valid for `size` bytes of
    // readable memory, which must be valid UTF-8.
    unsafe { ecalls::print(message, size) };
}

// define print! and println! macros that can be used by V-Apps
#[macro_export]
macro_rules! print {
    ($($arg:tt)*) => {{
        use core::fmt::Write;
        let mut buf = alloc::string::String::new();
        write!(&mut buf, $($arg)*).unwrap();
        $crate::print(buf.as_ptr(), buf.len());
    }};
}

#[macro_export]
macro_rules! println {
    () => ($crate::print!("\n"));
    ($($arg:tt)*) => ({
        $crate::print!("{}\n", format_args!($($arg)*));
    });
}

/// Initialization boilerplate for the application that is called before the main function, for
/// targets that need it.
#[macro_export]
macro_rules! bootstrap {
    () => {
        #[cfg(feature = "target_vanadium_ledger")]
        #[unsafe(no_mangle)]
        pub fn _start() {
            $crate::rust_init_heap();
            main()
        }

        #[cfg(feature = "target_vanadium_ledger")]
        use $crate::{print, println};
    };
}
