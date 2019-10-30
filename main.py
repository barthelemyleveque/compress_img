import sys
import cv2
import numpy as np
import random
import time
from centroids import  compute_centroids, init_centroids, find_closest_centroids
from tools import save_image, usage


def run_k_means(X, initial_centroids, iters):
    pixels = X.shape[0]
    k = initial_centroids.shape[0]
    idx = np.zeros(pixels)
    centroids = initial_centroids

    for i in range(iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)

    return idx, centroids

def compress_image(img, nb_colors):
    # Values are stocked line by line, in order to use clustering we'll stock them together, and reform them at the end
    X = np.reshape(img, (img.shape[0] * img.shape[1], img.shape[2]))
    initial_centroids = init_centroids(X, nb_colors)
    idx, centroids = run_k_means(X, initial_centroids, 10)
    idx = idx.astype(int)
    for i in range(X.shape[0]):
        X[i] = centroids[idx[i]]
    return X


# Check parameters are valid
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        return usage()
    filename = sys.argv[1]
    img = cv2.imread(filename, flags=cv2.IMREAD_COLOR)
    if (isinstance(img, np.ndarray) == 0):
        print("Invalid File\n")
        return usage()
    if len(sys.argv) == 3:
        if str.isdigit(sys.argv[2]):
            nb_colors = int(sys.argv[2])
        else:
            return usage()
    else:
        nb_colors = 16
    #normalization of data
    img = img / 255 
    X = compress_image(img, nb_colors)
    X_final =  np.reshape(X, (img.shape[0], img.shape[1], img.shape[2]))
    return save_image(X_final, filename, nb_colors)

if __name__ == '__main__':
    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()
    name = main()
    if (name != None):
        print("---  The image was compressed in %.2d seconds and saved as %s. ---" % ((time.time() - start_time), name))