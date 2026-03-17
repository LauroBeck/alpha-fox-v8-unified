#!/bin/bash
clear
echo "=========================================================="
echo "   ALPHA-FOX V8.3: FULL QUANTUM-FISCAL TITAN PIPELINE     "
echo "=========================================================="

# 1. Run Tech Projections (Python)
python3 /root/dev/alpha-fox-v8-unified/quantum/tech_titan_projections.py

# 2. Run Bank-to-Tech HPC Audit (C++20)
/root/dev/alpha-fox-v8-unified/bin/hpc_audit_engine

echo "=========================================================="
echo "   AUDIT COMPLETE: DATA SYNCED TO PRODUCTION LOGS         "
echo "=========================================================="
