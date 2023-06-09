from KNNData import KNNData
from Recommender import Recommender
from tabulate import tabulate

def main():
    knn_data = KNNData()
    
    print("Reading dataset")
    knn_data._read_dataset()
    
    print("Setting up variables and data")
    knn_data._setup()
    
    print("Decoding dataset")
    knn_data._decode()
    
    k = int(input("Enter a number K for KNN algorithm: "))
    print("Making recommender\n")
    recommender = Recommender(metric='cosine', algorithm='brute', k=k, data=knn_data.get_matrix_songs_features())
    
    try:
        # detect if fuzzy wuzzy cannot find the song input by user
        song_id, n_recommendations = prompt(knn_data=knn_data)
    except:
        print("\nProgram is going to terminate")
        return
    
    print(f"\nStarting the recommendation process...")
    song_name, song_artist, recommendations = make_recommendations(song_id=song_id, n_recommendations=n_recommendations, knn_data=knn_data, recommender=recommender)
    print_recommendations(song_name=song_name, song_artist=song_artist, recommendations=recommendations)
    return

def prompt(knn_data: KNNData):
    is_pass = False
    while not is_pass:
        song = str(input("Enter a song that you would like to get recommendation based on: "))
        try:
            found_song_id = knn_data.fuzzy_matching(song=song)
        except:
            print(f"The recommendation system could not find a match for {song} in dataset.")
            raise
        found_song = knn_data.get_decode_song()[found_song_id]
        if song != found_song:
            user_input = str(input(f"Is the song you are looking for \"{found_song}\"? (y for yes) "))
            if  user_input == 'y' or user_input == 'Y':
                is_pass = True
        else:
            is_pass = True
    n_recommendations=int(input("Enter the number of recommendations you would like: "))
    return found_song_id, n_recommendations

def make_recommendations(song_id: int, n_recommendations: int, knn_data: KNNData, recommender: Recommender):
    recommendations = list()
    recommended_id_list = recommender.make_recommendation(song_id=song_id, n_recommendations=n_recommendations)

    for index, songs_id_list in enumerate(recommended_id_list):
        recommendations.append([index, knn_data.get_decode_song()[songs_id_list[1]], knn_data.get_decode_artist()[songs_id_list[1]], 1 - songs_id_list[0]])

    song_name, song_artist = knn_data.get_decode_song()[song_id], knn_data.get_decode_artist()[song_id]
    return song_name, song_artist, recommendations

def print_recommendations(song_name, song_artist, recommendations):
    print(f"The recommendations for {song_name} from {song_artist} are:")
    print(tabulate(recommendations, headers=["#", "Song Name", "Artist", "Similarity"], floatfmt=".3f"))
    return

if __name__ == '__main__':
    main()