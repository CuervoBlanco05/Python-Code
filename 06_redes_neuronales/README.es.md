# 06. Redes neuronales: ejercicios guiados (NumPy → PyTorch)

>  [English version](README.md)

![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

Guías prácticas para **construir redes neuronales tú mismo**. Cada notebook explica la teoría y deja las
piezas clave del código como huecos `# TODO` para que los completes; una celda ✅ después de cada hueco
comprueba tu trabajo.

## Guías

| # | Notebook | Qué implementas |
|---|---|---|
| 01 | [`01_red_neuronal_desde_cero.ipynb`](01_red_neuronal_desde_cero.ipynb) | ReLU, softmax estable y entropía cruzada; *forward*, backpropagation derivada a mano y descenso de gradiente de un MLP en NumPy; el paso de entrenamiento; la misma red y su ciclo de entrenamiento en PyTorch, comparando tus gradientes con `autograd` |

Cada guía tiene su versión en inglés (`*_en.ipynb`).

## Cómo trabajar una guía

1. Lee la teoría e intenta primero las derivaciones en papel.
2. En cada celda ✍️, sustituye `raise NotImplementedError` por tu código.
3. Ejecuta la celda ✅ que viene después. Si falla, el mensaje te dice qué revisar.
4. Cuando pasen todas las comprobaciones, intenta los ejercicios extra del final.

Meta: más del 95 % de precisión en test con el dataset de tres espirales, y gradientes que coincidan con
PyTorch hasta ~10⁻¹⁶.

## Instalación

```bash
pip install -r requirements.txt  # desde la raíz del repo
jupyter lab
```

Los datos se generan dentro del notebook, así que no hace falta ningún archivo.
