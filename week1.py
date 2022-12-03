import csv
import random


def open_file(path):
    list_ = []
    with open(path) as csv_file:
        file = csv.DictReader(csv_file)
        for line in file:
            list_.append(line)
    return list_


def individual_choice(spotify_dataset):
    print("Please name 3 songs you have already listened to ")
    # ask user for input songs
    song_1 = str(input("Song 1: "))
    song_2 = str(input("Song 2: "))
    song_3 = str(input("Song 3: "))

    # flag variables to mark whether the input song is in the database
    flag_song_1 = "False"
    flag_song_2 = "False"
    flag_song_3 = "False"

    # keep repeating until all songs are found in the database
    while flag_song_1 == "False" and flag_song_2 == "False" and flag_song_3 == "False":

        for song in spotify_dataset:
            # check whether the first input song is in the database, and change value flag variable if true
            if song_1 == song['title']:
                flag_song_1 = "True"
                # check whether the second input song is in the database, and change value flag variable if true
            if song_2 == song['title']:
                flag_song_2 = "True"
            # check whether the third input song is in the database, and change value flag variable if true
            if song_3 == song['title']:
                flag_song_3 = "True"

            # if we have reached the last song in the database
            if song == spotify_dataset[-1]:
                # if the input songs have not been found ask the user for another song
                if flag_song_1 == "False":
                    song_1 = str(
                        input(f"Sorry, we could not recognise the song {song_1}, could you name another song? "))
                if flag_song_2 == "False":
                    song_2 = str(
                        input(f"Sorry, we could not recognise the song {song_2}, could you name another song? "))
                if flag_song_3 == "False":
                    song_3 = str(
                        input(f"Sorry, we could not recognise the song {song_3}, could you name another song? "))

    # change the value of the input songs to the dictionary of those input songs
    for song in spotify_dataset:
        if song_1 == song['title']:
            song_1 = song
        if song_2 == song['title']:
            song_2 = song
        if song_3 == song['title']:
            song_3 = song

    listened_songs = [song_1, song_2, song_3]

    # create a variable containing all the songs the user has listened to
    # this variable can be accessed outside of this function
    individual_choice.user_songs = listened_songs.copy()

    # create a list containing 100 playlists
    playlists = []
    for i in range(100):
        # each playlist consists of 50 songs
        random_playlist = random.sample(spotify_dataset, 50)
        # add every playlist to the list of playlists
        playlists.append(random_playlist)

    # variable that will be set to the 5 songs from a playlist that contains the input songs
    # if this variable stays 0, then we will know if such a playlist exists
    songs_5 = 0

    # go through every playlist
    for playlist in playlists:
        # check whether all the input songs are in the playlist
        if listened_songs[0] in playlist and listened_songs[1] in playlist and listened_songs[2] in playlist:
            # iterate over every song in the playlist
            for song in playlist:
                # generate 5 random songs from this playlist
                songs_5 = random.sample(playlist, 5)

                # check whether the 5 selected songs contain any of the input songs
                for new_song in songs_5:
                    if new_song in listened_songs:
                        # generate a different set of 5 songs
                        songs_5 = random.sample(playlist, 5)

    # if there is no playlist containing the input song
    if songs_5 == 0:
        print(
            "Sorry, we could not find a playlist with the songs you have already heard! But here are 5 songs you have never listened to:")
        # generate a random playlist
        playlist_songs_5 = random.choice(playlists)
        # generate 5 new songs from the random playlist
        songs_5 = random.sample(playlist_songs_5, 5)

        # check whether the 5 selected songs contain any of the input songs
        for new_song in songs_5:
            if new_song in listened_songs:
                # generate a different set of 5 songs
                songs_5 = random.sample(playlist_songs_5, 5)
        for new_song in songs_5:
            # print the title and artist of each of the 5 new songs generated
            print(f"{new_song['title']} by {new_song['artist']}")
            # add the new songs to the list of songs the user has listened to
            individual_choice.user_songs.append(new_song)

    # if there is a playlist with the input songs
    else:
        print("Here are 5 songs you have never listened to, from a playlist containing 3 songs you have listened to: ")
        for new_song in songs_5:
            # print the title and artist of each of the 5 new songs generated
            print(f"{new_song['title']} by {new_song['artist']}")
            # add the new songs to the list of songs the user has listened to
            individual_choice.user_songs.append(new_song)
