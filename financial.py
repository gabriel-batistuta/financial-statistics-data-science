import numpy as np
import modules as md
import pandas as pd

# Exemplo de dois vetores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# distancias das cidades
distance_eu = md.get_euclidian_distance(vector1, vector2)
distance_ma = md.get_manhattan_distance(vector1, vector2)
distance_min = md.get_minkowski_distance(vector1, vector2)

# Exemplo de dados de séries temporais
data = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', end='2024-05-01'),
    'Value': np.random.randn(121).cumsum()
})

md.get_serial_temporal_graph(data)

# exemplo de dados de grafico de velas
data_candles = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', end='2024-01-31'),
    'Open': np.random.rand(31),
    'High': np.random.rand(31) + 1,
    'Low': np.random.rand(31) - 1,
    'Close': np.random.rand(31)
})

md.get_graph_velas(data_candles)