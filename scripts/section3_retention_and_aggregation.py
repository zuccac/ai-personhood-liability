"""Section 3: Corollary 2 (retention) and Corollary 1 (aggregated deployers)."""
kH = 0.01
for rho in (0.0, 0.05, 1.0):
    print(f"retention {rho:4.0%}: developer's share of the benefit of care {kH + rho * (1 - kH):.2%} (observable safety), "
          f"{rho * (1 - kH):.2%} (hidden safety)")
q, kappa = 0.01, 0.017
a = (kappa - q) / (1 - q)
print(f"aggregated deployers, kappa = 1.7% of H, q = 1%: share through prices a = {a:.2%} (vs {kappa:.1%} single-unit)")
