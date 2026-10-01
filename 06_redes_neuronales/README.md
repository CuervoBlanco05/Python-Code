# 06. Neural Networks: Guided Exercises (NumPy → PyTorch)

>  [Versión en español](README.es.md)

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

Hands-on guides for **building neural networks yourself**. Each notebook explains the theory and leaves the
key pieces of code as `# TODO` gaps for you to fill in; a ✅ cell after each gap checks your work.

## Guides

| # | Notebook (EN) | Notebook (ES) | What you implement |
|---|---|---|---|
| 01 | [`01_neural_network_from_scratch_en.ipynb`](01_neural_network_from_scratch_en.ipynb) | [`01_red_neuronal_desde_cero.ipynb`](01_red_neuronal_desde_cero.ipynb) | ReLU, stable softmax and cross-entropy; forward pass, hand-derived backpropagation and gradient descent for an MLP in NumPy; the training step; the same network and training loop in PyTorch, with your gradients compared against `autograd` |

## How to work through a guide

1. Read the theory section and try the derivations on paper first.
2. In every ✍️ cell, replace `raise NotImplementedError` with your code.
3. Run the ✅ cell that follows it. If it fails, its message tells you what to check.
4. Once every check passes, try the extra exercises at the end.

Target: above 95 % test accuracy on the three-spirals dataset, and gradients that match PyTorch to about 10⁻¹⁶.

## Setup

```bash
pip install -r requirements.txt  # from the repo root
jupyter lab
```

The data is generated inside the notebook, so no files are needed.
