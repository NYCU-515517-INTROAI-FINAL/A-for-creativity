from SpotifyClient import SpotifyClient
from sklearn.pipeline import Pipeline
from scipy.spatial.distance import cdist
import numpy as np

class Recommender:
    def __init__(self):
        # initialize variables list
        self.number_cols = None
        self.spotify_api = None
        self.song_cluster_pipeline = None
        return
    
    def _setup(self, spotify_api: SpotifyClient, song_cluster_pipeline: Pipeline):
        self.number_cols = ["valence", "year", "acousticness", "danceability", "duration_ms", "energy", "explicit", 
                            "instrumentalness", "key", "liveness", "loudness", "mode", "popularity", "speechiness", "tempo"]
        self.spotify_api = spotify_api
        self.song_cluster_pipeline = song_cluster_pipeline
        return
    
    def _get_song_data(self, song, dataset):
        try:
            song_data = dataset[(dataset["name"] == song["name"]) & (dataset["year"] == song["year"])].iloc[0]
            song_data = song_data.to_frame().T
        except IndexError:
            print(f'The song {song["name"]} which is released in {song["year"]} cannot be find in dataset.')
            print("Serching on Spotify with Spotify API")
            song_data = self.spotify_api.find_song(song["name"], song["year"])
        return song_data
    
    def _get_mean_vector(self, song_list, dataset):
        song_vectors = []
        for song in song_list:
            song_data = self._get_song_data(song, dataset)
            if song_data is None:
                print("Warning: {} does not exist in Spotify or in database".format(song["name"]))
                continue
            song_vector = song_data[self.number_cols].values
            song_vectors.append(song_vector)
        
        song_matrix = np.array(list(song_vectors))
        return np.mean(song_matrix, axis=0)
    
    def _flatten_dict_list(self, dict_list):
        flattened_dict = dict()
        for key in dict_list[0].keys():
            flattened_dict[key] = []
        
        for dictionary in dict_list:
            for key, value in dictionary.items():
                flattened_dict[key].append(value)

        return flattened_dict
    
    def make_recommendations(self, song_list, dataset, n_recommendations):
        metadata_cols = ["name", "year", "artists"]
        song_dict = self._flatten_dict_list(song_list)
        song_center = self._get_mean_vector(song_list, dataset)
        scaler = self.song_cluster_pipeline.steps[0][1]
        scaled_data = scaler.transform(dataset[self.number_cols])
        scaled_song_center = scaler.transform(song_center.reshape(1, -1))
        distances = cdist(scaled_song_center, scaled_data, "cosine")
        distances_list = distances.tolist()[0]
        index = list(np.argsort(distances)[:, :n_recommendations][0])
        
        rec_songs = dataset.iloc[index]
        rec_songs = rec_songs[~rec_songs["name"].isin(song_dict["name"])]
        recommendations = rec_songs[metadata_cols].to_dict(orient="records")
        for i, i_distance in enumerate(index):
            recommendations[i]['similarity'] = 1 - distances_list[int(i_distance)]
        for i in range(len(recommendations)):
            recommendations[i]['artists'] = recommendations[i]['artists'].replace('[', '').replace(']', '').replace('\'', '\"')
        return recommendations