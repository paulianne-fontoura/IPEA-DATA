# -*- coding: utf-8 -*-
"""API query publishes IPEA DATA for calculation of accumulated IPCA index

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A5hjI9ubkAo0zoGAM2gyzmmxML2i-rw0
"""

!pip install ipeadatapy
import ipeadatapy as ip

ip.list_series()

ip.list_series('IPCA')

ip.describe('PRECOS12_IPCA12')

ip.timeseries('PRECOS12_IPCA12')

ip.timeseries('PRECOS12_IPCA12',
              yearGreaterThan = 2020).plot('RAW DATE', 'VALUE (-)',
                                                               kind = 'bar',
                                                               figsize = (15, 10))

ip.timeseries('PRECOS12_IPCA15G12')

import numpy as np

# Series data
series = {
    "Série 1": [-0.0013, 0.0001, -0.0012, -0.0004, 0.0034, 0.0032, 0.0065, 0.005, 0.0081, 0.0013, 0.0026, 0.0043, 0.0017],
    "Série 2": [6659.95, 6667.94, 6683.28, 6700.66, 6716.74, 6735.55, 6773.27, 6801.72, 6858.17, 6869.14, 6895.24, 6926.96, 6941.51],
    "Série 3": [0.0004, -0.0007, 0.0028, 0.0035, 0.0021, 0.0033, 0.004, 0.0031, 0.0078, 0.0036, 0.0021, 0.0044, 0.0039],
    "Série 4": [-0.0008, 0.0012, 0.0023, 0.0026, 0.0024, 0.0028, 0.0056, 0.0042, 0.0083, 0.0016, 0.0038, 0.0046, 0.0021],
    "Série 5": [0.0069, -0.0101, 0.0111, 0.0047, 0.0002, 0.0048, 0.0034, 0.0025, 0.0027, 0.0019, -0.0001, 0.0067, 0.0025]
}

# Cumulative indices for series 1, 3, 4 and 5
def calcular_acumulado(taxas_mensais):
    return np.prod([1 + taxa for taxa in taxas_mensais])

# Calculation for the series
resultados = {}
for nome, dados in series.items():
    if nome == "Série 2":
        # Cumulative indices (direct calculation)
        fator = dados[-1] / dados[0]
    else:
        # Monthly fees (cumulative calculation)
        fator = calcular_acumulado(dados)
    resultados[nome] = fator

# Calculated results
resultados