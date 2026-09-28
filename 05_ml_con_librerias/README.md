# 05. Applied Machine Learning (Pandas · Polars · Scikit-Learn · PyTorch)

> 🇪🇸 [Versión en español](README.es.md)

![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Polars](https://img.shields.io/badge/Polars-CD792C?style=flat&logo=polars&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

An end-to-end, hands-on learning path: the **same problem** (house-price prediction) is solved step by step
with industry-standard tools. It complements `03_ml_from_scratch`, where the algorithms are implemented from first principles.

## 🧭 Learning path

| # | Notebook (EN) | Notebook (ES) | What it covers |
|---|---|---|---|
| 01 | [`01_pandas_and_polars_en.ipynb`](01_pandas_and_polars_en.ipynb) | [`01_pandas_y_polars.ipynb`](01_pandas_y_polars.ipynb) | Loading, exploring, cleaning and aggregating data; Polars expression API and *lazy* queries; Pandas ↔ Polars cheat sheet |
| 02 | [`02_scikit_learn_en.ipynb`](02_scikit_learn_en.ipynb) | [`02_scikit_learn.ipynb`](02_scikit_learn.ipynb) | Leak-free `Pipeline` + `ColumnTransformer`, cross-validated model comparison, `GridSearchCV`, metrics, permutation importance, classification |
| 03 | [`03_pytorch_en.ipynb`](03_pytorch_en.ipynb) | [`03_pytorch.ipynb`](03_pytorch.ipynb) | Tensors, autograd, gradient descent, MLP with a custom training loop and early stopping, saving/loading weights |

Every notebook ends with ✏️ **exercises**.

## 📊 Results

| Model | Evaluation | RMSE | R² |
|---|---|---|---|
| Linear regression (baseline) | 5-fold CV on train | ~33,100 | 0.900 |
| Histogram Gradient Boosting, untuned | 5-fold CV on train | ~24,400 | 0.945 |
| Histogram Gradient Boosting, tuned (scikit-learn) | held-out test set | ~20,100 | 0.960 |
| MLP neural network (PyTorch) | held-out test set | ~19,300 | 0.964 |

On small tabular data, a tuned gradient-boosting model performs on par with a neural network at a fraction of the effort.
The notebooks discuss when deep learning is worth it.

## 📦 Data

`datos/houses.csv` (English columns) and `datos/casas.csv` (Spanish columns) contain the same **synthetic** dataset
(2,000 houses) with numeric and categorical features and deliberately injected missing values.
The ground-truth relationship is known, which makes it easy to validate models. Regenerate both with:

```bash
python datos/generar_datos.py
```

## ⚙️ Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # from the repo root
jupyter lab
```

> Run the notebooks from this folder (`05_ml_con_librerias/`) so that the `datos/...` paths resolve.
> For GPU-enabled PyTorch, see https://pytorch.org/get-started/locally/.

## 🚀 Next steps
1. Apply the notebook 02 workflow to a real dataset (Kaggle, UCI, `sklearn.datasets.fetch_california_housing`).
2. PyTorch for images: `torchvision` + MNIST / CIFAR-10 with convolutional networks.
3. Experiment tracking (MLflow) and dedicated gradient-boosting libraries (XGBoost, LightGBM).
4. Physics-informed neural networks (PINNs) in PyTorch, connecting with `02_scientific_computing`.
