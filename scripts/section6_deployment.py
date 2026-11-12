"""Proposition 9 (deployment at given care): example with H = EUR 1m, kappa = EUR 10k, q = 1%, pi = 0.1%."""
H, k, q, pi = 1e6, 1e4, 0.01, 0.001
pbar = q + (1 - q) * pi
print(f"social cost per deployment            EUR {H * pbar:,.0f}")
print(f"capped deployer, no developer liability  EUR {k * pbar:,.0f}")
print(f"capped deployer, full residual liability EUR {k * pbar + pi * (1 - q) * (H - k):,.0f}")
print(f"aggregated deployers + developer         EUR {(1 - pi) * q * H + pi * k + pi * (H - k):,.0f}")
print(f"prefunded capital cost at c = 5%         EUR {0.05 * (H - k):,.0f}")
