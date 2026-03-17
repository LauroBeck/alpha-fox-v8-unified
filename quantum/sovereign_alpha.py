import numpy as np
import json
import os
from qiskit_finance.applications.optimization import PortfolioOptimization
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import SamplingVQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler as Sampler # Patch for Qiskit 1.x
from qiskit.circuit.library import n_local

def run_multi_bank_quantum_projection():
    print("\n--- 2026 ALPHA-FOX: MULTI-BANK QUANTUM PROJECTION (V8.2) ---")
    
    # Banks under audit
    banks = ["JPM", "MS", "BNY", "CITI", "JEFF", "UBS", "WELLS"]
    mu = np.array([0.08, 0.07, 0.06, 0.09, 0.11, 0.05, 0.07]) 
    
    # B-PIPE Pulse Integration
    brent_price = 104.15
    penalty = (brent_price - 80) / 100
    mu = mu * (1 - penalty)
    
    print(f"B-PIPE Sync: Brent ${brent_price} | Tech Anchor (IBM): $249.25")

    num_assets = len(mu)
    sigma = np.eye(num_assets) * 0.05
    
    portfolio = PortfolioOptimization(expected_returns=mu, covariances=sigma, risk_factor=0.25, budget=4)
    qp = portfolio.to_quadratic_program()
    
    # Using the StatevectorSampler for reliable local execution
    sampler = Sampler()
    ansatz = n_local(num_assets, rotation_blocks='ry', entanglement_blocks='cz', reps=3)
    
    vqe = SamplingVQE(sampler=sampler, ansatz=ansatz, optimizer=COBYLA())
    optimizer = MinimumEigenOptimizer(vqe)
    result = optimizer.solve(qp)

    print("\n--- Projected Bank Exposure (Quantum Optimized) ---")
    for i, bank in enumerate(banks):
        status = "ALLOCATED" if result.x[i] > 0.5 else "HEDGED"
        print(f"{bank:5}: {status}")
    
    print(f"\nFinal Quantum Alpha Score: {result.fval:.4f}")

if __name__ == "__main__":
    run_multi_bank_quantum_projection()
