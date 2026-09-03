# ECE 8803-AI4 — Course Notebooks

Notebooks for the course, one folder per module. Each module is self-contained: its notebook,
its datasets, and its own README with a Colab link.

| module | topic | notebook |
|---|---|---|
| [Module 6 — Statistical Process Control](Module%206%20SPC/) | capability, control charts, gauge R&R, multivariate FDC, run-to-run control | [`statistical-process-control.ipynb`](Module%206%20SPC/statistical-process-control.ipynb) |
| [Module 7 — Virtual Metrology](Module%207%20Virtual%20Metrology/) | predicting a measurement from trace features, leakage, drift, the metrology noise floor, deployment | [`virtual-metrology.ipynb`](Module%207%20Virtual%20Metrology/virtual-metrology.ipynb) |

*(further modules added as the semester goes)*

## Running the notebooks

**In Colab** — open the module folder and click its Colab badge. The first cell downloads that
module's datasets, so nothing needs to be uploaded by hand. Do **File → Save a copy in Drive**
before editing, or your changes are lost when the tab closes.

**Locally** — clone once and everything comes with it:

```bash
git clone https://github.com/aikhan123/ece8803-ai4-notebooks.git
cd "REPO/Module 6 SPC"
jupyter lab statistical-process-control.ipynb
```

Python 3.10 or newer with `numpy`, `pandas`, `scipy`, `matplotlib` and `scikit-learn`. With
Anaconda you already have all five. To pick up notebooks added later, `git pull`.

## Layout

```
<module-name>/
├── README.md          what the module covers, Colab link
├── <module-name>.ipynb
└── data/              every CSV the notebook reads
```

Notebooks are committed with their outputs saved, so you can read the results before running
anything. Run them yourself to reproduce — simulations use fixed seeds, so the numbers match.
