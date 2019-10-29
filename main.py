import sys
import cv2
import numpy as np
import random

def compute_centroids(X, idx, k):
    pixels, n = X.shape
    centroids = np.zeros((k,n))
    

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



def run_k_means(X, initial_centroids, iters):
    pixels, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(pixels)
    centroids = initial_centroids

    for i in range(iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)

    return idx, centroid

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

def compress_image(img, nb_colors):
    # Values are stocked line by line, in order to use clustering we'll stock them together, and reform them at the end
    X = np.reshape(img, (img.shape[0] * img.shape[1], img.shape[2]))
    print(X.shape)
    initial_centroids = init_centroids(X, nb_colors)
    print(initial_centroids)
    idx, centroids = run_k_means(X, initial_centroids, 10)
    return (X)

def usage():
    print("Usage :\npython main.py [image_file] [number_of_colors](optional, 16 by default)")

# Check parameters are valid
def main():
    if len(sys.argv) <= 2 or len(sys.argv) > 3:
        return usage()
    filename = sys.argv[1]
    img = cv2.imread(filename, flags=cv2.IMREAD_COLOR)
    if len(sys.argv) == 3:
        if str.isdigit(sys.argv[2]):
            nb_colors = int(sys.argv[2])
        else:
            return usage()
    else:
        nb_colors = 16
    #normalization of data
    img = img / 255 
    compress_image(img, nb_colors)

if __name__ == '__main__':
    main()