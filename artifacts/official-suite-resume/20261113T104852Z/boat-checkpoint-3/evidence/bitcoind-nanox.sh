#!/bin/sh
# Real public Bitcoin Core; isolate RPC/P2P ports for the second complete device suite.
exec /var/lib/orb-node/work/official-suite-resume/bitcoin-core/bitcoin-32.1/bin/bitcoind -rpcport=19443 -port=19444 "$@"
