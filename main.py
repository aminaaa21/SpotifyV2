# imports
from week1 import open_file, individual_choice

spotify_dataset = open_file('spotify-dataset.csv')  # a dictionary containing all the information about the songs

if __name__ == '__main__':
    individual_choice(spotify_dataset)
