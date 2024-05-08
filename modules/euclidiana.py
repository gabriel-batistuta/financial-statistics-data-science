from scipy.spatial.distance import minkowski, cityblock, euclidean
import numpy as np

# Exemplo de dois vetores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

def get_euclidian_distance(vector1, vector2):
    # Medida de distância de Minkowski com p=2 (Euclidiana)
    euclidean_distance = minkowski(vector1, vector2, p=2)
    print("Distância Euclidiana:", euclidean_distance)
    return euclidean_distance