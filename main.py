# imports
from week1 import open_file, individual_choice
from week3 import Song, count_moods, ChooseSongs
import pandas
spotify_dataset = open_file('spotify-dataset.csv')  # a dictionary containing all the information about the songs


# pandas example
df = pandas.read_csv('spotify-dataset.csv', header=0, index_col=0)
title = str(df.sample().index[0])
title = 'The Hills'
flag_song = title in df.index
song_info = df.loc[title]
happy_songs = df.loc[df['Valence - The higher the value, the more positive mood for the song'] > 75]
s = happy_songs.sample(5)


if __name__ == '__main__':
    # individual_choice(spotify_dataset)
    song_1 = Song(song_info)
    mood_1 = song_1.mood()
    print(song_1.title, song_1.info.artist)
    songs_per_mood = count_moods(mood_1, n_songs=5)
    recommended = ChooseSongs(df).by_mood(songs_per_mood)
    print(recommended)

