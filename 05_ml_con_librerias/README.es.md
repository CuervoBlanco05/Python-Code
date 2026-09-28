# 05. Machine Learning con librerías (Pandas · Polars · Scikit-Learn · PyTorch)

>  [English version](README.md)

Ruta de aprendizaje práctica: el **mismo problema** (predecir el precio de una casa) se resuelve paso a paso
con las herramientas estándar de la industria. Complementa a `03_ml_from_scratch`, donde los algoritmos se
implementan desde cero.

## Ruta de aprendizaje

| # | Notebook | Qué aprendes |
|---|---|---|
| 01 | [`01_pandas_y_polars.ipynb`](01_pandas_y_polars.ipynb) | Cargar, explorar, limpiar, agrupar; API de expresiones y modo *lazy* de Polars; chuleta Pandas ↔ Polars |
| 02 | [`02_scikit_learn.ipynb`](02_scikit_learn.ipynb) | `train_test_split`, `Pipeline`, `ColumnTransformer`, validación cruzada, `GridSearchCV`, métricas, importancia de variables, clasificación |
| 03 | [`03_pytorch.ipynb`](03_pytorch.ipynb) | Tensores, autograd, regresión con descenso de gradiente, red neuronal (MLP), ciclo de entrenamiento, *early stopping* |

Cada notebook termina con **ejercicios** para practicar. Cada uno tiene su versión en inglés (`*_en.ipynb`).

## 📦 Datos

`datos/casas.csv` es un dataset **sintético** (2 000 casas) con variables numéricas, categóricas y valores
faltantes a propósito (`datos/houses.csv` es el mismo con columnas en inglés). Se regeneran con:

```bash
python datos/generar_datos.py
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # desde la raíz del repo
jupyter lab
```

> Ejecuta los notebooks desde esta carpeta (`05_ml_con_librerias/`) para que las rutas `datos/...` funcionen.
> Para PyTorch con GPU, consulta el comando de instalación en https://pytorch.org/get-started/locally/.

## Siguientes pasos sugeridos
1. Aplicar el flujo del notebook 02 a un dataset real (Kaggle, UCI, `sklearn.datasets.fetch_california_housing`).
2. PyTorch con imágenes: `torchvision` + MNIST / CIFAR-10 y redes convolucionales.
3. Seguimiento de experimentos (MLflow) y modelos de gradient boosting dedicados (XGBoost, LightGBM).
4. Redes informadas por la física (PINNs) con PyTorch, conectando con `02_scientific_computing`.
