from sklearn.neighbors import NearestNeighbors

class Recommender:
    def __init__(self, metric, algorithm, k, data):
        self.metric = metric
        self.algorithm = algorithm
        self.k = k
        self.data = data
        self.model = None
        return
    
    def make_recommendation(self, song_id, n_recommendations):
        recommendations = list()
        self.model = NearestNeighbors(metric=self.metric, algorithm=self.algorithm, n_neighbors=self.k, n_jobs=-1).fit(self.data)
        distances, indices = self.model.kneighbors(self.data[song_id], n_neighbors=n_recommendations+1)
        for i in range(1, len(distances[0])):
            recommendations.append([distances[0][i], indices[0][i]])
        return recommendations