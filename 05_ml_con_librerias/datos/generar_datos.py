"""Genera un dataset sintético de precios de casas para los notebooks de aprendizaje.

Se usa un dataset sintético para no depender de descargas y para saber
exactamente qué relación hay entre las variables (útil para validar modelos).

Uso:
    python generar_datos.py            # crea casas.csv en esta carpeta
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEMILLA = 42
N_CASAS = 2_000
BARRIOS = {"Centro": 1.35, "Norte": 1.15, "Sur": 0.90, "Periferia": 0.75}


def generar(n: int = N_CASAS, semilla: int = SEMILLA) -> pd.DataFrame:
    rng = np.random.default_rng(semilla)

    barrio = rng.choice(list(BARRIOS), size=n, p=[0.2, 0.3, 0.3, 0.2])
    metros = rng.normal(110, 35, n).clip(35, 350).round(1)
    habitaciones = np.clip((metros / 35 + rng.normal(0, 0.8, n)).round(), 1, 7).astype(int)
    antiguedad = rng.integers(0, 60, n)
    distancia_centro_km = np.where(
        barrio == "Centro", rng.uniform(0, 3, n), rng.uniform(2, 25, n)
    ).round(2)
    tiene_cochera = rng.random(n) < 0.45

    # Relación "verdadera" (no lineal) que los modelos deben descubrir
    factor_barrio = np.vectorize(BARRIOS.get)(barrio)
    precio = (
        25_000
        + 1_900 * metros
        + 9_000 * habitaciones
        - 45 * antiguedad**2
        - 2_500 * np.sqrt(distancia_centro_km) * 10
        + 18_000 * tiene_cochera
    ) * factor_barrio
    precio = precio + rng.normal(0, 15_000, n)
    precio = precio.clip(30_000).round(-2)

    df = pd.DataFrame(
        {
            "id": np.arange(1, n + 1),
            "barrio": barrio,
            "metros": metros,
            "habitaciones": habitaciones,
            "antiguedad": antiguedad,
            "distancia_centro_km": distancia_centro_km,
            "tiene_cochera": np.where(tiene_cochera, "si", "no"),
            "precio": precio,
        }
    )

    # Datos "sucios" a propósito para practicar limpieza
    faltantes_metros = rng.choice(n, size=int(0.04 * n), replace=False)
    faltantes_antig = rng.choice(n, size=int(0.03 * n), replace=False)
    df.loc[faltantes_metros, "metros"] = np.nan
    df.loc[faltantes_antig, "antiguedad"] = np.nan
    return df


if __name__ == "__main__":
    salida = Path(__file__).with_name("casas.csv")
    generar().to_csv(salida, index=False)
    print(f"Dataset guardado en {salida}")
