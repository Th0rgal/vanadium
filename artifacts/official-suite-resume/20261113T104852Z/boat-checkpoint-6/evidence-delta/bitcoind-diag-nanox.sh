#!/bin/sh
exec /var/lib/orb-node/work/official-suite-resume/bitcoin-core/bitcoin-32.1/bin/bitcoind -rpcport=21443 -port=21444 "$@"
