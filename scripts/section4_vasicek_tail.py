"""Section 4 footnote: in a one-factor large-pool model with failure probability p = 1%,
the share of the marginal harm from care lying beyond the 99.5% quantile."""
import numpy as np
from scipy.stats import norm
from scipy import integrate

p, alpha = 0.01, 0.005


def share(rho):
    a = norm.ppf(p)
    dL = lambda z: norm.pdf((a - np.sqrt(rho) * z) / np.sqrt(1 - rho)) / np.sqrt(1 - rho) / norm.pdf(a) * norm.pdf(z)
    tail = integrate.quad(dL, -np.inf, norm.ppf(alpha), limit=200)[0]
    total = integrate.quad(dL, -np.inf, np.inf, limit=200)[0]
    return tail / total


for rho in (0.01, 0.1, 0.25, 0.5):
    print(f"asset correlation {rho:.2f}: share beyond the quantile {share(rho):.1%}")
