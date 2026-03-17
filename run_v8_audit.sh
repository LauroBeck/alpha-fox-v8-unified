#!/bin/bash
echo "--- INITIALIZING V8.1 UNIFIED QUANTUM-FISCAL PIPELINE ---"
cd /root/dev/alpha-fox-v8-unified

# 1. Start Stargate Listener
python3 stargate/stargate_listener.py > stargate/pulse.log 2>&1 &
ST_PID=$!
sleep 2

# 2. Run Quantum Multi-Bank Alpha Engine
python3 quantum/sovereign_alpha.py

# 3. Run Fiscal C++ Validation
./bin/alpha_fox_suite

# 4. Graceful Cleanup
kill $ST_PID 2>/dev/null
echo "--- AUDIT COMPLETE ---"
