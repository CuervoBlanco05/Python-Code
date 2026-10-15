# Python Scientific & Algorithmic Code Reference

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-High_Performance-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Overview
This repository serves as a structured collection of algorithms, numerical methods, data structures, and Machine Learning concepts implemented from first principles in Python.

It acts as a personal code library for performance benchmarking, scientific computing experiments, and technical reference for production analytics.

---

## 🗂️ Repository Structure

```text
.
├── 01_algorithms_and_ds/       # Graph traversal, sorting, and optimization algorithms
├── 02_scientific_computing/    # Numerical integration, linear algebra & vectorization
├── 03_ml_from_scratch/         # Gradient descent, KNN, and Neural Networks built without high-level APIs
├── 04_benchmarking/            # Execution speed comparisons (Cpython vs. Numba vs. JAX)
└── 05_ml_con_librerias/        # Applied ML path (EN/ES): Pandas & Polars → Scikit-Learn → PyTorch
```

Install dependencies with `pip install -r requirements.txt`.
---

### 🛠️ Key Topics Covered
* Core Algorithms: Sorting, searching, recursion, dynamic programming, and complexity analysis ($\mathcal{O}(n)$ evaluation).
* Mathematical Methods: Matrix decompositions, root-finding algorithms, and statistical modeling.
* Vectorization & Speed: Transitioning standard loops into vectorized operations using NumPy and JAX acceleration.
* OOP & Design Patterns: Object-oriented design applied to data processing pipelines.

---
###  Author
Pablo Adrián Cárdenas Mendívil (Cuervo Blanco)

M.Sc. in Physics | Quantum ML & High-Performance Data Engineering

GitHub: @CuervoBlanco05

---
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300" shape-rendering="crispEdges">
  <!-- Fondo -->
  <rect width="400" height="300" fill="#0d1117"/>

  <!-- Ventana de terminal -->
  <rect x="80" y="60" width="240" height="160" fill="#1e1e2e"/>
  <rect x="80" y="60" width="240" height="20" fill="#3a3a4a"/>
  <rect x="90" y="66" width="8" height="8" fill="#ff5f56"/>
  <rect x="104" y="66" width="8" height="8" fill="#ffbd2e"/>
  <rect x="118" y="66" width="8" height="8" fill="#27c93f"/>

  <!-- Texto de la terminal -->
  <text x="95" y="105" font-family="monospace" font-size="14" fill="#39ff14">$ whoami</text>
  <text x="95" y="125" font-family="monospace" font-size="14" fill="#39ff14">&gt; gato_pixel</text>
  <text x="95" y="145" font-family="monospace" font-size="14" fill="#39ff14">$ _</text>

  <!-- Cursor parpadeando -->
  <rect x="125" y="133" width="9" height="14" fill="#39ff14">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>

  <!-- Gato pixel (sentado, de frente) -->
  <rect x="300" y="170" width="10" height="10" fill="#f5a623"/>  <!-- oreja izq -->
  <rect x="340" y="170" width="10" height="10" fill="#f5a623"/>  <!-- oreja der -->
  <rect x="300" y="180" width="50" height="40" fill="#f5a623"/>  <!-- cabeza -->
  <rect x="312" y="192" width="8" height="8" fill="#0d1117"/>    <!-- ojo izq -->
  <rect x="330" y="192" width="8" height="8" fill="#0d1117"/>    <!-- ojo der -->
  <rect x="320" y="206" width="10" height="6" fill="#e0701a"/>   <!-- nariz -->
  <rect x="305" y="220" width="40" height="40" fill="#f5a623"/>  <!-- cuerpo -->
  <rect x="300" y="260" width="20" height="10" fill="#e0701a"/>  <!-- pata izq -->
  <rect x="330" y="260" width="20" height="10" fill="#e0701a"/>  <!-- pata der -->
  <rect x="350" y="240" width="10" height="10" fill="#f5a623"/>  <!-- cola -->
  <rect x="360" y="230" width="10" height="20" fill="#f5a623"/>  <!-- cola -->
</svg>
