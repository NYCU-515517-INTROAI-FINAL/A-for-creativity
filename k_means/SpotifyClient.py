import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self, client_id, client_secret):
        try:
            client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
            self.spotify = spotipy.Spotify(auth_manager=client_credentials_manager)
            self.spotify.search(q= "track: Stay Away year: 1993", limit=1) # for detection if connection is build
            return
        except spotipy.oauth2.SpotifyOauthError:
            print("Did not find Spotify credentials.")
            print("Please check your \".env\" file.")
            raise
        
    def find_song(self, name, year):
        song_data = dict()
        results = self.spotify.search(q= "track: {} year: {}".format(name,year), limit=1)
        if results["tracks"]["items"] == []:
            return None

        results = results["tracks"]["items"][0]
        track_id = results["id"]
        audio_features = self.spotify.audio_features(track_id)[0]

        song_data["name"] = [name]
        song_data["year"] = [year]
        song_data["explicit"] = [int(results["explicit"])]
        song_data["duration_ms"] = [results["duration_ms"]]
        song_data["popularity"] = [results["popularity"]]
        for key, value in audio_features.items():
            song_data[key] = value
        return pd.DataFrame(song_data)