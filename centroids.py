import numpy as np
import random

# Update centroids
def compute_centroids(X, idx, k):
    pixels, n = X.shape
    centroids = np.zeros((k,n))
    for i in range(k):
        nb_samples = 0
        for j in range(pixels):
            if idx[j] == i:
                nb_samples += 1
                centroids[i] += X[j]
        centroids[i] = centroids[i] / nb_samples
    
    return centroids


def find_closest_centroids(X, centroids):
    pixels = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(pixels)

    for i in range(pixels):
        closest_centroid = 0
        #euclidean distance
        min_d = np.linalg.norm(X[i] - centroids[0])
        for j in range(k):
            d = np.linalg.norm(X[i] - centroids[j])
            if d < min_d:
                min_d = d
                closest_centroid = j
        idx[i] = closest_centroid
    return idx

def init_centroids(X, k):
    pixels, n = X.shape
    centroids = np.zeros((k, n))
    used_c = []
    for i in range(k):
        c = random.randint(0, pixels - 1)
        while c in used_c:
            c = random.randint(0, pixels -1)
        used_c.append(c)
        centroids[i]  = X[c]
    return centroids