import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self, client_id, client_secret):
        try:
            client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
            self.spotify = spotipy.Spotify(auth_manager=client_credentials_manager)
            self.spotify.search(q= "track: Stay Away year: 1993", limit=1) # for detection if connection is build
            return
        except spotipy.oauth2.SpotifyOauthError:
            print('Did not find Spotify credentials.')
            print('Please check your ".env" file.')
            raise