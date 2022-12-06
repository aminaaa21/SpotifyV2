import pandas as pd


class Song:
    """
    Song class
    """

    def __init__(self, info):
        """Takes in the song's info.

        :param info: The song's info from the dataset (pd.Series) or if the song has multiple duplicate song names the
            dataframe containing the song info (pd.DataFrame)
        """

        if type(info) != pd.Series:
            # Duplicate value (like 'The Hills'), so the same song is in the database multiple times.
            info = info.iloc[0]
        self.title = info.index
        self.info = info
        print(info['the genre of the track'])

    def genre(self):
        # get genre from song info
        song_genre = self.info['the genre of the track']
        # check if it's pop, rock or techno
        # TODO rest of this (week2)
        return song_genre

    def mood(self):
        """Returns the mood of the song as a list with mood(s)."""

        # happy: high valence
        happy = self.info['Valence - The higher the value, the more positive mood for the song']
        # party: high danceability
        party = self.info['Danceability - The higher the value, the easier it is to dance to this song']
        # calming: low energy
        calming = 100 - self.info['Energy- The energy of a song - the higher the value, the more energtic']
        # lounge: high acoustic
        lounge = self.info['Acousticness - The higher the value the more acoustic the song is']

        # sort the moods based on their values from high to low
        moods = (('happy', happy), ('party', party), ('calming', calming), ('lounge', lounge))
        moods_sorted = sorted(moods, key=lambda key: key[1], reverse=True)

        # add the first mood type to the list of moods
        song_moods = [moods_sorted[0][0]]
        # loop through the mood types, and if the mood is close enough to the first mood and higher than 50, add it to
        # the list of moods
        for i in range(1, len(moods_sorted)):
            if (moods_sorted[0][1] - moods_sorted[i][1]) < 20 and moods_sorted[i][1] > 50:
                song_moods.append(moods_sorted[i][0])
        # return the generated list of moods
        return song_moods


def count_moods(moods_list, n_songs=5):
    # TODO could be a 'count_type' function if Song.genre would exist
    """Counts the number of each mood type in a list of mood types, then normalizes to the number of songs required."""

    # define the possible moods in a dictionary, starting with 0 songs per mood
    songs_per_mood = {'happy': 0, 'party': 0, 'calming': 0, 'lounge': 0}
    # variables needed for the loop
    total, chosen_songs = len(moods_list), 0
    # loop through all mood types and add the n songs of the mood type to the songs_per_mood dictionary
    for mood_type in songs_per_mood:
        songs_per_mood[mood_type] = int(moods_list.count(mood_type) / total * n_songs)
        chosen_songs += songs_per_mood[mood_type]
    # this loop checks if the required number of songs is met
    while chosen_songs < n_songs:
        # if the required number of songs isn't met, add one to the mood type with the most songs
        songs_per_mood[max(songs_per_mood, key=lambda key: songs_per_mood[key])] += 1
        chosen_songs += 1
    # return the dictionary with the number of songs per mood
    return songs_per_mood


class ChooseSongs:
    """
    Song choosing class
    """

    def __init__(self, dataset):
        """Takes in a dataset of songs.

        :param dataset: A dataset containing songs with info (pd.DataFrame)
        """

        self.df = dataset

    def by_mood(self, songs_per_mood):
        """Selects songs by mood, given a dictionary with how many songs per mood should be chosen."""

        # select the rows with songs meeting the requirements for each mood type
        songs = {
            # happy: high valence
            'happy':
                self.df.loc[self.df['Valence - The higher the value, the more positive mood for the song'] > 75],
            # party: high danceability
            'party':
                self.df.loc[self.df['Danceability - The higher the value, the easier it is to dance to this song']
                            > 75],
            # calming: low energy
            'calming':
                self.df.loc[self.df['Energy- The energy of a song - the higher the value, the more energtic'] <= 25],
            # lounge: high acousticness
            'lounge':
                self.df.loc[self.df['Acousticness - The higher the value the more acoustic the song is'] > 75]
        }

        # loop through the moods and add n randomly chosen songs from the songs dictionary to the list of songs, where
        # n is the number of songs in the dictionary from the input
        songs_list = []
        for song_type in songs_per_mood:
            chosen_songs = songs[song_type].sample(songs_per_mood[song_type])
            songs_list += list(chosen_songs.index.values)
        # return a list of song titles
        return songs_list
