
from __future__ import division
import random
import numpy as np
import time

 
def init_board(n):
    return np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(n)])


def assign_points(dataset, centers):
    clusters = {}
    
    for tupel in dataset:
        best_center_key = min([(key, np.linalg.norm(tupel - center)) \
            for key, center in enumerate(centers)], key=lambda x: x[1])[0]

        try:
            clusters[best_center_key].append(tupel)
        except KeyError:
            clusters[best_center_key] = [tupel]

    return clusters

def recompute_centers(centers, clusters):
    converged = True

    new_centers = []

    for center_key in clusters:
        new_cluster_center = np.mean(clusters[center_key], axis=0)

        if (new_cluster_center != centers[center_key]).all():
            converged = False

        new_centers.append(new_cluster_center) 

    return converged, new_centers

 
def initialize(X, K):
    C = random.sample(X, 1)
    for k in range(1, K):
        D2 = np.array([min([np.linalg.norm(c-x) for c in C]) for x in X])
        probs = D2/D2.sum()
        cumprobs = probs.cumsum()
        r = np.random.rand()
        for j,p in enumerate(cumprobs):
            if r < p:
                i = j
                break
        C.append(X[i])
    return C


def kmeans(dataset, k, fn=None):
    
    if not fn:
        centers = random.sample(dataset, k)
    else:
        centers = fn(dataset, k)


    while True:
        clusters = assign_points(dataset, centers)
        converged, new_centers = recompute_centers(centers, clusters)

        if converged:
            break
        
        centers = new_centers

    return centers, clusters


def cluster_iris(): 
    iris_dataset = np.loadtxt('../data/iris.csv', delimiter=',')[0:,0:-1]
    centers, clusters = kmeans(iris_dataset, 3);
    print len(clusters[0])
    print len(clusters[1])
    print len(clusters[2])
    centers, clusters = kmeans(iris_dataset, 3, initialize);
    print len(clusters[0])
    print len(clusters[1])
    print len(clusters[2])

def cluster_cloud(): 
    dataset = np.loadtxt('../data/cloud.data')
    start = time.clock()
    centers, clusters = kmeans(dataset, 6);
    end = time.clock()
    print end - start
    print len(clusters[0])
    print len(clusters[1])
    print len(clusters[2])
    start = time.clock()
    centers, clusters = kmeans(dataset, 6, initialize);
    end = time.clock()
    print end - start
    print len(clusters[0])
    print len(clusters[1])
    print len(clusters[2])
 
   

if __name__ == '__main__':
    cluster_cloud()
