import numpy as np
import random

random.seed(7)
np.random.seed(7)

def get_initial_prototypes(X, k):
    number_of_samples = X.shape[0]
    all_ids = [i for i in range(X.shape[0])]
    random.shuffle(all_ids)
    prototypes = all_ids[:k]
    return prototypes

def get_clusters(X, prototypes):
    X_selective = X[:,prototypes]
    closest_cluster_ids = np.argmin(X_selective, axis=1)
    clusters = {}
    for i in range(len(prototypes)):
        clusters[i] = []
    for i, cluster_id in enumerate(closest_cluster_ids):
        clusters[cluster_id].append(i)
    return clusters

def update_prototypes(X, clusters):
    prototypes = []
    total_cost = 0.0
    labels = [0 for i in range(X.shape[0])]
    for i in range(len(clusters)):
        print('here')
        cluster = clusters[i]
        print(X)
        print(cluster)
        X_selective = X[cluster, cluster]
        distance_sum = np.sum(X_selective, axis = 1)
        new_prototype = np.argmin(distance_sum)[0]
        cur_cost = np.min(distance_sum)
        total_cost += cur_cost
        prototypes[i] = cluster[new_prototype]
        for c in cluster:
            labels[c] = cluster[new_prototype]
    return prototypes, total_cost, labels

def perform_k_means_algorithm(X, k, movement_threshold_delta=0):
    print('suck my balls')
    new_prototypes = get_initial_prototypes(X, k)
    should_terminate = False
    new_cost = np.sum(X)
    labels = []
    while not should_terminate:
        previous_prototypes = new_prototypes
        previous_cost = new_cost
        clusters = get_clusters(X, previous_prototypes)
        new_prototypes, new_cost, labels = update_prototypes(X, clusters)
        should_terminate = (previous_cost - new_cost < movement_threshold_delta)
    return new_prototypes, labels