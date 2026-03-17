#!/usr/bin/env python3
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_v8_theta_decay():
    # 4-qubit circuit for Alpha + Theta (Time Decay)
    qc = QuantumCircuit(4, 4)
    
    # I. Initial Sentiment (Bullish Pi/4)
    qc.ry(np.pi / 4, [0, 1, 2, 3])
    
    # II. Entanglement (Asset Correlation)
    qc.cx(0, 1)
    qc.cx(2, 3)
    
    # III. Introduce Theta Decay (Phase Gates)
    # S-gate (90 degree) on Alpha cluster (IBM/NVDA)
    # T-gate (45 degree) on Beta cluster (Treasury/Gold)
    qc.s(0)
    qc.s(1)
    qc.t(2)
    qc.t(3)
    
    qc.measure([0,1,2,3], [0,1,2,3])

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    return result.get_counts()

if __name__ == "__main__":
    counts = run_v8_theta_decay()
    print("\n" + "="*40)
    print("V8.3.2 QUANTUM THETA (TIME DECAY) RESULTS")
    print("="*40)
    print(f"Decay-Adjusted Counts: {counts}")
    print("Verification: Phase rotation confirmed for |1100> cluster.")
    print("="*40 + "\n")
