import numpy as np

def project_alpha_2026():
    print("\n--- TECH TITAN ALPHA PROJECTION: 2026 CLUSTER ROI ---")
    
    # Current Anchors (March 16, 2026)
    tech_stack = {
        "NVIDIA": {"price": 183.22, "weight": 0.40, "vol": 0.25},
        "IBM":    {"price": 249.25, "weight": 0.20, "vol": 0.15},
        "MSFT":   {"price": 420.15, "weight": 0.25, "vol": 0.18},
        "ORCL":   {"price": 165.30, "weight": 0.15, "vol": 0.22}
    }

    simulations = 10000
    time_horizon = 1.0 # 1 Year
    
    print(f"{'Ticker':<10} | {'Current':<10} | {'Proj. 2027 High':<15} | {'Risk Score'}")
    print("-" * 55)

    for ticker, data in tech_stack.items():
        # GBM (Geometric Brownian Motion) Simulation
        drift = 0.12 # Assuming 12% baseline AI growth
        stdev = data['vol']
        
        periodic_returns = np.exp((drift - 0.5 * stdev**2) + stdev * np.random.normal(0, 1, simulations))
        projected_price = data['price'] * periodic_returns.mean()
        risk_score = (stdev * 100) / (drift * 10)
        
        print(f"{ticker:<10} | ${data['price']:<9.2f} | ${projected_price:<14.2f} | {risk_score:.2f}")

if __name__ == "__main__":
    project_alpha_2026()
