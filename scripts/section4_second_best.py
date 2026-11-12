"""Proposition 6 (second-best retention): closed form against a brute-force search."""
import numpy as np
from scipy.optimize import minimize_scalar


def rho_star(pi0, c, ystar=0.5, kh=0.01, hidden=False):
    B = 1.0
    km = pi0 * B / ystar
    base = B if hidden else B * (1 - kh)
    first = 0.0 if hidden else B * kh

    def social(rho):
        lam = first + rho * base
        y = minimize_scalar(lambda y: km * y**2 / 2 + pi0 * (1 - y) * lam, bounds=(0, 1), method="bounded").x
        return km * y**2 / 2 + pi0 * (1 - y) * B + c * rho * base

    grid = np.linspace(0, 1, 2001)
    numeric = grid[np.argmin([social(r) for r in grid])]
    formula = max(0.0, 1 - c / (pi0 * ystar * (1 - (0 if hidden else kh))))
    return numeric, formula


for pi0, c in [(0.01, 0.05), (0.10, 0.01), (0.20, 0.05)]:
    print(f"pi0 = {pi0:.0%}, c = {c:.0%}: rho* numeric {rho_star(pi0, c)[0]:.3f}, formula {rho_star(pi0, c)[1]:.3f}")
print(f"threshold for pi0 = 1%, y* = 0.5, kappa/H = 1%: c < {0.01 * 0.5 * 0.99:.3%}")
