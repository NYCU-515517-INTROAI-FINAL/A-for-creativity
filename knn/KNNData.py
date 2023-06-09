import pandas as pd
from scipy.sparse import csr_matrix
from fuzzywuzzy import fuzz

class KNNData:
    def __init__(self):
        # initialize variables list
        ## will be use in readfile function
        self.dataset = "https://drive.google.com/uc?id=11IBLzjtTwvL9kbywjgugsjpFASDvU3Ox&confirm=t&uuid=f6de33d0-0a77-4367-bb5b-e33cdf39b06c&at=AKKF8vxw2T6yJn2isQjBlML7moea:1684571748628"
        self.songs = pd.DataFrame()
        
        ## first be assignd in setup function
        self.song_user = None
        self.song_ten_id = None
        self.song_id_more_ten = None
        self.songs_features = None
        self.matrix_songs_features = None
        self.unique_songs = None
        
        ## first be assigned in decode
        self.decode_id = None
        self.decode_song = dict()
        self.decode_artist = dict()
        return
    
    def _read_dataset(self):
        self.songs = pd.read_csv(self.dataset)
        self.songs.drop("song", inplace=True, axis=1)
        return

    def _setup(self):
        self.song_user = self.songs.groupby('user_id')['song_id'].count()
        self.song_ten_id = self.song_user[self.song_user>16].index.to_list()
        self.song_id_more_ten = self.songs[self.songs['user_id'].isin(self.song_ten_id)].reset_index(drop=True)
        self.songs_features = self.song_id_more_ten.pivot(index='song_id', columns='user_id', values='listen_count').fillna(0)
        self.matrix_songs_features = csr_matrix(self.songs_features.values)
        self.unique_songs = self.songs.drop_duplicates(subset=['song_id']).reset_index(drop=True)[['song_id', 'title', 'artist']]
        return
    
    def _decode(self):
        self.decode_id = {
            song : i for i, song in
            enumerate(list(self.unique_songs.set_index('song_id').loc[self.songs_features.index].title))
        }

        size = len(self.unique_songs)
        song_id = [0]*size
        artist = [0]*size

        unique_title = self.unique_songs.set_index('song_id').loc[self.songs_features.index].title
        unique_artist = self.unique_songs.set_index('song_id').loc[self.songs_features.index].artist
        for i in range(size):
            song_id[i] = unique_title[i]
            artist[i] = unique_artist[i]
        for i in range(size):
            self.decode_song[i] = song_id[i]
            self.decode_artist[i] = artist[i]
        return
    
    def fuzzy_matching(self, song):
        match_tuple = list()
        
        # get match
        for title, item in self.decode_id.items():
            ratio = fuzz.ratio(title.lower(), song.lower())
            if ratio >= 60:
                match_tuple.append((title, item, ratio))

        # sort
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            raise
        return match_tuple[0][1]
    
    def get_matrix_songs_features(self):
        return self.matrix_songs_features
    
    def get_decode_id(self):
        return self.decode_id
    
    def get_decode_song(self):
        return self.decode_song
    
    def get_decode_artist(self):
        return self.decode_artist