import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

class KMeansData:
    def __init__(self):
        # initialize the variables list
        self.dataset_link = "https://drive.google.com/uc?id=1wwGiv96gPqP9zu2CpJiaM_vePVl1v3bJ&export=download"
        self.dataset = pd.DataFrame()
        
        # be assigned in train function
        self.song_cluster_pipeline = None
        self.X = None
        self.song_cluster_labels = None
        return
    
    def _read_dataset(self):
        self.dataset = pd.read_csv(self.dataset_link)
        return
    
    def _train(self, n_clusters):
        self.song_cluster_pipeline = Pipeline([("scaler", StandardScaler()), 
                                               ("kmeans", KMeans(n_clusters=n_clusters, verbose=False))], verbose=False)
        X = self.dataset.select_dtypes(np.number)
        self.song_cluster_pipeline.fit(X)
        self.song_cluster_labels = self.song_cluster_pipeline.predict(X)
        return
    
    def visualize_dataset_clusters(self):
        # Visualizing the Clusters with PCA
        pca_pipeline = Pipeline([("scaler", StandardScaler()), ("PCA", PCA(n_components=2))])
        song_embedding = pca_pipeline.fit_transform(self.X)
        projection = pd.DataFrame(columns=["x", "y"], data=song_embedding)
        projection["title"] = self.dataset["name"]
        projection["cluster"] = self.dataset["cluster_label"]

        fig = px.scatter(projection, x="x", y="y", color="cluster", hover_data=["x", "y", "title"])
        fig.show()
    
    def get_song_cluster_labels(self):
        return self.song_cluster_labels
    
    def get_song_cluster_pipeline(self):
        return self.song_cluster_pipeline
    
    def get_dataset(self):
        return self.dataset