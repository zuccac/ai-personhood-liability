"""Section 5 calibration (consolidated capital, Proposition 7; capital multiplier, Proposition 8(i);
cost of capital). Exact binomial calculation with Q = 1,000 units.
Parameters: p0 = 2%, H = 1, k = 0.04."""
import numpy as np
from scipy.stats import binom

p0, H, k, Q = 0.02, 1.0, 0.04, 1000
xs = np.linspace(0, 1, 2001)


def loss_per_unit(x, kappa, n):
    """l_n(x, kappa) = E[min(n kappa, H D_n)] / n with D_n ~ Bin(n, p0 (1 - x))."""
    d = np.arange(n + 1)
    pmf = binom.pmf(d, n, p0 * (1 - x))
    return float(np.sum(pmf * np.minimum(n * kappa, H * d))) / n


def care(kappa, n):
    costs = [k * x**2 / 2 + loss_per_unit(x, kappa, n) for x in xs]
    return xs[int(np.argmin(costs))]


xstar = p0 * H / k
Sstar = p0 * H - (p0 * H) ** 2 / (2 * k)

if __name__ == "__main__":
    print(f"first-best care x* = {xstar:.3f}, accident probability {p0 * (1 - xstar):.3%}, S* = {Sstar:.4f}")
    print(f"capital multiplier H/S* = {H / Sstar:.1f}")
    print(f"care with consolidated capital 0.010 per unit (Q = {Q}): {care(0.010, Q):.3f}")
    print(f"care with consolidated capital 0.017 per unit (Q = {Q}): {care(0.017, Q):.3f}")
    print(f"care under full fragmentation at kappa = H: {care(1.0, 1):.3f}")
    saving = p0 * H - Sstar
    print(f"saving from care S(0) - S* = {saving:.4f}; optimal floor (Proposition 2) is zero from c = {p0**2 * H / k:.2%}")
    print(f"at c = 5%: capital H costs {0.05 * H:.4f} per unit, capital S* costs {0.05 * Sstar:.5f}")
