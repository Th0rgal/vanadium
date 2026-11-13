set pagination off
set confirm off
set print thread-events off
set architecture arm
set tcp auto-retry on
set tcp connect-timeout 30
set remotetimeout 20
file /var/lib/orb-node/work/official-suite-resume/speculos-candidate-runtime/speculos/resources/launcher
target remote 127.0.0.1:1236
handle SIGILL nostop noprint pass
add-symbol-file /var/lib/orb-node/work/official-suite-resume/app-bitcoin/build/nanox/bin/app.elf 0x40000000
hbreak *0x400136c6
commands
 silent
 printf "\nDIAG_GUEST_OS_LONGJMP exception=%u LR=0x%08x PC=0x%08x SP=0x%08x R9=0x%08x\n", $r0,$lr,$pc,$sp,$r9
 info registers
 x/12i $lr-16
 x/48wx $sp
 bt 24
 continue
end
hbreak *0x40013cdc
commands
 silent
 printf "\nDIAG_GUEST_OS_SCHED_EXIT code=%u LR=0x%08x PC=0x%08x SP=0x%08x R9=0x%08x\n", $r0,$lr,$pc,$sp,$r9
 info registers
 x/12i $lr-16
 x/48wx $sp
 bt 24
 continue
end
break sys_os_sched_exit
commands
 silent
 printf "\nDIAG_LAUNCHER_OS_SCHED_EXIT code=%u LR=0x%08x PC=0x%08x SP=0x%08x\n",$r0,$lr,$pc,$sp
 info registers
 set $ctx=*(unsigned int*)0xf01b9a2c
 printf "DIAG_SAVED_UCONTEXT 0x%08x\n",$ctx
 x/28wx $ctx
 x/64wx $sp
 bt 24
 continue
end
continue
printf "\nDIAG_GDB_CONTINUE_RETURNED\n"
info program
