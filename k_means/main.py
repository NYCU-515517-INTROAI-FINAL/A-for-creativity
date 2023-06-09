from KMeansData import KMeansData

def main():
    print("Setting link of dataset")
    k_means_data = KMeansData()
    
    print("Reading dataset")
    k_means_data._read_dataset()
    
    print("Training model")
    k_means_data._train(n_clusters=20)
    return

if __name__ == '__main__':
    main()