# Personhood for AI Entities: code for the numerical results

Code for the paper "Personhood for AI Entities: Fragmentation, Correlation, and Capital" by Claudio Zucca (European Investment Bank and Luxembourg School of Business). The scripts reproduce every number and the figure in the paper.

## Requirements

Python 3.10 or later with numpy, scipy and matplotlib:

```
pip install -r requirements.txt
```

## Running

```
python scripts/run_all.py
```

This runs every script in about 20 seconds and writes Figure 1 to `output/fig_retention.pdf`. Each script can also be run on its own from the `scripts` folder.

| Script | What it reproduces |
| --- | --- |
| `model1_calibration.py` | Section 5 calibration: S* = 0.015, the multiplier H/S* of about 67, care near zero with capital 0.010 and 0.483 with capital 0.017 (exact binomial, Q = 1,000), and the cost-of-capital comparison |
| `model1_entity_size.py` | Proposition 8(iii): the threshold f-bar (about 0.0006), optimal entity sizes of 2 to 7 units for f between 0.001 and 0.0125, 89% to 98% of the liability shield kept, care below 0.05 |
| `section3_retention_and_aggregation.py` | Corollary 2 (a 5% retention gives a share of 5.95%) and Corollary 1 (share through prices of 0.71% with aggregated deployers) |
| `section4_vasicek_tail.py` | Section 4 footnote: share of marginal harm beyond the 99.5% quantile in a one-factor model, 0.9% to 9.4% |
| `section4_second_best.py` | Proposition 6: second-best retention, closed form checked against a brute-force search |
| `section6_deployment.py` | Proposition 9 example: social cost of EUR 10,990 per deployment against EUR 110 and EUR 1,090 |
| `figure1_retention.py` | Figure 1: retention delivered by each capital rule |

All parameter values are illustrative and are not estimates for actual companies.

## AI assistance

The code was written with the help of Claude (Anthropic), as declared in the paper. The author reviewed it and takes responsibility for it.

## Licence

MIT. See `LICENSE`.
