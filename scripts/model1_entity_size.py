"""Proposition 8(iii) and the Section 5 calibration of entity size: threshold f-bar,
optimal entity size, share of the liability shield kept, and care, with kappa = S*."""
import numpy as np
from model1_calibration import p0, H, k, Sstar, loss_per_unit

kappa = Sstar
xs = np.linspace(0, 1, 4001)
W, X = {}, {}
for n in range(1, 41):
    c = [k * x**2 / 2 + loss_per_unit(x, kappa, n) for x in xs]
    i = int(np.argmin(c)); W[n], X[n] = c[i], xs[i]

fbar = min(n / (n - 1) * (W[n] - W[1]) for n in range(2, 41))
print(f"Delta = W2 - W1 = {W[2] - W[1]:.6f}; f-bar = {fbar:.6f} ({fbar:.3%} of H)")
print(" f        n*  shield kept  care")
for f in (0.0003, 0.0006, 0.001, 0.0025, 0.005, 0.0075, 0.01, 0.0125):
    n = min(W, key=lambda m: W[m] + f / m)
    print(f" {f:.4f}  {n:3d}   {(Sstar - W[n]) / (Sstar - W[1]):6.1%}     {X[n]:.3f}")
