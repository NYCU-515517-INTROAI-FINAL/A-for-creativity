import pandas as pd

class KMeansData:
    def __init__(self):
        self.dataset_link = "https://drive.google.com/uc?id=1wwGiv96gPqP9zu2CpJiaM_vePVl1v3bJ&export=download"
        self.dataset = pd.DataFrame()
        return
    
    def _read_dataset(self):
        self.dataset = pd.read_csv(self.dataset_link)
        return