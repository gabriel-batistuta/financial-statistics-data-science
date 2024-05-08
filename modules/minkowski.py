from scipy.spatial.distance import minkowski, cityblock, euclidean
import numpy as np

def get_minkowski_distance(vector1, vector2):
    # Medida de distância de Minkowski com p=3
    minkowski_distance = minkowski(vector1, vector2, p=3)
    print("Distância de Minkowski (p=3):", minkowski_distance)
    return minkowski_distance