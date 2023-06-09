from KMeansData import KMeansData
from SpotifyClient import SpotifyClient
from Recommender import Recommender
from dotenv import load_dotenv
from tabulate import tabulate

import pandas as pd
import os
import warnings

def main():
    print("Turning off warning messages")
    warnings.filterwarnings("ignore")
    
    print("Setting link of dataset")
    k_means_data = KMeansData()
    
    print("Reading dataset")
    k_means_data._read_dataset()
    
    print("Training model")
    k_means_data._train(n_clusters=20)
    
    # load .env file and get id and secret if exist
    if os.path.exists("./.env"):
        load_dotenv() # load .env file
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
    else:
        print("Error: You haven't create the \".env\" file from \".env.example\" file")
        return
    
    # build the connection with spotify api
    try:
        print("Connecting to Spotify")
        spotify_api = SpotifyClient(client_id=client_id, client_secret=client_secret)
        print("Spotify api connected")
    except:
        print("Error: Your Spotify ID or Secret might be incorrect")
        return
    
    # process the input songs
    filename = "input_songs.csv"
    
    print(f"Reading \"{filename}\"")
    input_songs = pd.read_csv(filename, dtype={"name": str, "year": int})
    input_songs = input_songs.to_dict('records')
    
    print("\nYour input songs are: ")
    print(tabulate(input_songs))
    
    # recommendation process
    n_recommendations = int(input("\nEnter the number of recommendations you would like: "))

    print("Initializing recommender")
    recommender = Recommender()
    
    print("Setting up recommender")
    recommender._setup(spotify_api=spotify_api, song_cluster_pipeline=k_means_data.get_song_cluster_pipeline())
    
    print("making recommendations")
    recommendations = recommender.make_recommendations(song_list=input_songs, dataset=k_means_data.get_dataset(), n_recommendations=n_recommendations)
    rows =  [x.values() for x in recommendations]
    
    print("\nThe reommendation songs are: ")
    print(tabulate(rows, headers=["Name", "Year", "Artist", "Similarity"]))
    return

if __name__ == '__main__':
    main()