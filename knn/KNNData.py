from Recommender import Recommender
import pandas as pd

class KNNData:
    def __init__(self):
        self.dataset = "https://drive.google.com/uc?id=11IBLzjtTwvL9kbywjgugsjpFASDvU3Ox&confirm=t&uuid=f6de33d0-0a77-4367-bb5b-e33cdf39b06c&at=AKKF8vxw2T6yJn2isQjBlML7moea:1684571748628"
        return
    
    def _read_file(self):
        self.songs = pd.read_csv(self.dataset)
        self.songs.drop("song", inplace=True, axis=1)
        return
