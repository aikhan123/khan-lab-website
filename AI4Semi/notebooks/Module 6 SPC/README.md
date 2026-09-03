# Module 6 — Statistical Process Control

Statistical process control worked end to end on a semiconductor gate-CD process: capability
and variance budgets, X̄–R and I–MR charts, autocorrelation, gauge R&R, residual charting,
multivariate fault detection with PCA, and a run-to-run control loop.

Everything is computed from the CSVs in `data/` — nothing is hard-coded, so you can change a
dataset, a window or a rule set and watch the conclusions move.

## Run it in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aikhan123/ece8803-ai4-notebooks/blob/main/Module%206%20SPC/statistical-process-control.ipynb)

Colab opens the notebook but not the data, so run the first cell — it downloads the nine CSVs
automatically. Everything the notebook imports (numpy, pandas, scipy, matplotlib) is already
installed in Colab; there is nothing to `pip install`. Do **File → Save a copy in Drive**
before you edit anything.

## Run it locally

```bash
git clone https://github.com/aikhan123/ece8803-ai4-notebooks.git
cd "REPO/Module 6 SPC"
jupyter lab statistical-process-control.ipynb
```

Python 3.10 or newer with `numpy`, `pandas`, `scipy` and `matplotlib`.

## What the notebook covers

**Foundations** — characterising a process against specification; the variance budget and
which component is worth attacking; why subgroup means are √n quieter than individuals; what
happens when every lot is corrected on its own measurement.

**Charts and capability** — building X̄–R charts and reading run rules; the same data as
individuals and what the metrology budget costs you in detection; why an autocorrelated but
perfectly healthy process fires 26 alarms; choosing limits and rules from the relative cost of
false alarms and missed shifts.

**Measurement, cases and multivariate** — gauge R&R and why its two acceptance metrics can
disagree; correcting a capability number for the gauge that produced it; charting the residual
from a known drift instead of the raw signal; PCA-based T² and SPE monitoring with
contribution plots; and what a run-to-run controller hides from the chart everyone watches.

## Datasets

| file | contents |
|---|---|
| `hw1_cd_individuals.csv` | 100 lots, one gate-CD measurement each |
| `hw2_cd_subgroups.csv` | 30 lots × 5 wafers |
| `hw2_etch_ar1.csv` | 200 lots of autocorrelated etch rate |
| `hw2_probe_yield.csv` | 30 lots of probe yield, varying die count |
| `hw3_gauge_study_A.csv` | gauge R&R, CD-SEM #1: 10 parts × 3 tools × 2 trials |
| `hw3_gauge_study_B.csv` | gauge R&R, CD-SEM #2 |
| `hw3_etch_seasoning.csv` | 120 lots with chamber seasoning and PM resets |
| `hw3_fdc.csv` | 200 runs × 12 correlated sensors |
| `hw3_r2r_loop.csv` | 120 lots through an EWMA run-to-run controller |

The datasets are synthetic, generated from models of real fab behaviour.
