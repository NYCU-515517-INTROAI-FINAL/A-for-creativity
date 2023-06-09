from KMeansData import KMeansData
from SpotifyClient import SpotifyClient
from dotenv import load_dotenv
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
    
    return

if __name__ == '__main__':
    main()