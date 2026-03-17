#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# 1. Rebuild the v8.3.2 Theta Engine State
qc = QuantumCircuit(4)
qc.ry(np.pi / 4, [0, 1, 2, 3]) # Sentiment Tilt
qc.cx(0, 1)                    # Asset Correlation
qc.cx(2, 3)
qc.s(0)                        # S-gate (90° Phase Decay)
qc.s(1)
qc.t(2)                        # T-gate (45° Phase Decay)
qc.t(3)

# 2. Extract the Statevector (The mathematical "Soul" of the target)
state = Statevector(qc)

# 3. Plot Bloch Spheres and Save to File
fig = plot_bloch_multivector(state, title="Alpha-Fox V8.3.2: Bloch Target Projections")
fig.savefig('quantum_bloch_targets.png')

print("\n" + "="*40)
print("3D BLOCH PROJECTION COMPLETE")
print("="*40)
print("File saved: quantum_bloch_targets.png")
print("Visual: Rotation on Q0/Q1 represents the $280.95 Price Phase.")
print("="*40 + "\n")
