# Defect Classification — companion notebooks

Reproduce, from scratch, every figure in the two Defect Classification lectures.

## Files
- `module 3 lecture 1.ipynb` — Lecture 1: *The Obvious Approach and What It Hides*
  (wafer data, logistic regression from first principles, deep neural networks, the CNN).
- `module 3 lecture 2.ipynb` — Lecture 2: *Physics Beats Parameters, Until It Doesn't*
  (polar features + random forest, the head-to-head, the preprocessing bug).
- `wm811k_dev.npz` — the development subset (~26,000 wafer maps) both notebooks use.

## Run
Open a notebook in this folder and run top to bottom. The `DATA` variable at the top is
already set to `wm811k_dev.npz` in this folder, so no path change is needed.

Lecture 1 takes ~5–6 minutes (it trains two small networks live); Lecture 2 takes ~25 s.

## Requirements
    python3 -m pip install numpy matplotlib scikit-learn pandas
PyTorch is optional — only the CNN training cell in Lecture 1 needs it, and that cell is
switched off by default (`RUN_CNN = False`) with the lecture's reported numbers printed
instead.

## Notes
Models trained live here run on the ~26K development subset, so their numbers differ
slightly from the full-test-set figures quoted on the slides; each is labelled as such,
and the pattern (which model wins where) is identical.

Data set: M.-J. Wu, J.-S. R. Jang, J.-L. Chen, "Wafer Map Failure Pattern Recognition and
Similarity Ranking for Large-Scale Data Sets," IEEE Trans. Semiconductor Manufacturing,
28(1), 1–12, 2015. doi:10.1109/TSM.2014.2364237
