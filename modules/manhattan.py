from scipy.spatial.distance import minkowski, cityblock, euclidean
import numpy as np

def get_manhattan_distance(vector1, vector2):
    # Medida de distância de Minkowski com p=1 (Manhattan)
    manhattan_distance = minkowski(vector1, vector2, p=1)
    print("Distância Manhattan:", manhattan_distance)
    return manhattan_distance