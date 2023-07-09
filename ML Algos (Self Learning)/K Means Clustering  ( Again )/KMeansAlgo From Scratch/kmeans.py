# decide cluster 
# select random centroid 
# assign clusters
# check finish

class Kmeans:
    def __init__(self,num_clusters=2,max_iter=100):
        self.num_clusters = num_clusters
        self.max_iter = max_iter
        self.centroids = None 
    
    def fit_predict(self,x):
        print(x)