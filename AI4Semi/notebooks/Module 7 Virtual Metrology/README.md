# Module 7 — Virtual Metrology

Virtual metrology worked end to end on a semiconductor gate-etch process: building features from
raw sensor traces, the baseline any model has to beat, ridge / lasso / PLS on 120 columns, the
noise floor your metrology sets — and then the harder half, which is finding out whether the model
actually works. Leakage from lots and from time, drift across a chamber clean, charting the
residual, budgeting the error, and what accuracy permits you to deploy.

Two problem sets: **HW1** builds the model, **HW2** takes it apart.

Everything is computed from the CSVs in `data/` — nothing is hard-coded, so you can change a
split, a window or a threshold and watch the conclusions move.

## Run it in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aikhan123/ece8803-ai4-notebooks/blob/main/Module%207%20Virtual%20Metrology/virtual-metrology.ipynb)

Colab opens the notebook but not the data, so run the first cell — it downloads the six CSVs
automatically. Everything the notebook imports (numpy, pandas, matplotlib, scikit-learn) is
already installed in Colab; there is nothing to `pip install`. Do **File → Save a copy in Drive**
before you edit anything.

## Run it locally

```bash
git clone https://github.com/aikhan123/ece8803-ai4-notebooks.git
cd "REPO/Module 7 Virtual Metrology"
jupyter lab virtual-metrology.ipynb
```

Python 3.10 or newer with `numpy`, `pandas`, `matplotlib` and `scikit-learn`.

## What the notebook covers

**HW1 — build the model.** Segmenting traces by recipe step and summarising each window, and why
your columns will not match somebody else's; the previous-measurement baseline, computed before
any model; ridge, lasso, PLS and gradient boosting on the same folds; choosing the number of PLS
components with the one-standard-error rule; reading which feature block the model leans on; the
RMSE floor and R² ceiling that the CD-SEM sets; and a stuck sensor that a rolling variance check
finds and a one-off check does not.

**HW2 — find out whether it works.** The same model evaluated four ways — random, lot-grouped,
leave-one-chamber-out and time-ordered — and what each gap is made of; scoring against the
baseline on the same wafers, where the honest advantage collapses; an I–MR chart on the prediction
residual with limits from held-out data, and which run rule catches the chamber clean first;
splitting the error into the gauge's share and the model's own, with remedies aimed at drift
rather than capacity; the EWMA gain a run-to-run controller should use on a noisier input; and a
deployment proposal argued from the numbers.

## Datasets

| file | contents |
|---|---|
| `vm_features.csv` | 1200 wafers: identifiers, chamber state, `recipe_complete`, 120 feature columns |
| `vm_labels.csv` | 465 CD-SEM measurements, with tool and measurement time |
| `vm_events.csv` | the chamber maintenance log — five cleans, with run numbers |
| `vm_traces_subset.csv` | raw 1 Hz traces for 60 wafers: five sensors, three recipe steps |
| `vm_gauge_study.csv` | CD-SEM repeatability study, 15 wafers × 6 repeats |
| `vm_feature_dictionary.csv` | every `f###` column, its block and its physical meaning |

Feature blocks: `f000`–`f039` sensor (5 sensors × 2 steps × 4 statistics, computed from the
traces), `f040`–`f059` lot-level (constant within a lot), `f060`–`f119` nuisance.

The process is one etch tool with two chambers, gate CD in nanometres, target 45.0 nm and
specification 43.0 – 47.0 nm. The datasets are synthetic, generated from models of real fab
behaviour — including the things the problems ask you to find.
