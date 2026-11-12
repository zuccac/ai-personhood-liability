"""Figure 1 (fig_retention.pdf): retention delivered by each capital rule, large N.
Developer's loss: X with probability pi (binary) or U*X with U ~ Beta (dispersed)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy import integrate
alpha, r = 0.005, 0.95
def rho_beta(pi, a, b):
    if pi <= alpha: return 0.0
    U = beta(a, b); u = U.ppf(1 - alpha/pi)
    return integrate.quad(lambda z: min(z, u)*U.pdf(z), 0, 1, limit=200, points=[u])[0]/U.mean()
grid = np.round(np.concatenate([np.linspace(1e-4, .005, 25), np.linspace(.00505, .03, 120)]), 6)
x = 100*grid
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(5.6, 3.2))
ax.plot(x, [r]*len(x), color="0.6", lw=1.3, ls="--", label="Recovery target $r=95\\%$")
ax.plot(x, grid, color="0.6", lw=1.3, label="Expected-loss capital")
ax.plot(x, (grid > alpha).astype(float), color="#1f4e9c", lw=2, label="99.5% ruin rule, defect hits all deployments")
ax.plot(x, [rho_beta(p, 2, 2) for p in grid], color="#1f4e9c", lw=1.2, ls="--", label="99.5% ruin rule, random share, Beta(2,2)")
ax.plot(x, [rho_beta(p, .75, .75) for p in grid], color="#1f4e9c", lw=1.2, ls=":", label="99.5% ruin rule, random share, Beta(0.75,0.75)")
ax.axvline(0.5, color="0.6", ls=":", lw=1)
ax.text(0.45, 0.3, "$\\pi=\\alpha$", fontsize=8, color="0.3", ha="right")
ax.set_xlim(0, 3); ax.set_ylim(-0.02, 1.05)
ax.set_xlabel("Defect probability $\\pi$ (%)")
ax.set_ylabel("Retention $\\rho$ delivered by the rule")
ax.grid(axis="y", color="0.9")
ax.legend(frameon=False, fontsize=7.5, loc="center right")
fig.tight_layout(); fig.savefig("../output/fig_retention.pdf")
