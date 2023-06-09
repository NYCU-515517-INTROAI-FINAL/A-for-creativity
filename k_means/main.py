from KMeansData import KMeansData
def main():
    print("Setting link of dataset")
    k_means_data = KMeansData()
    
    print("Reading dataset")
    k_means_data._read_dataset()
    return

if __name__ == '__main__':
    main()