class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song_instance):
        if song_instance.genre not in cls.genres:  # Check if the instance's genre is in the genres list
            cls.genres.append(song_instance.genre)

    @classmethod
    def add_to_artists(cls, song_instance):
        if song_instance.artist not in cls.artists:  # Corrected: appending to artists list, not genres
            cls.artists.append(song_instance.artist)

    @classmethod
    def add_to_genre_count(cls, song_instance):
        if cls.genre_count.get(song_instance.genre):  # If the genre is already in the dictionary
            cls.genre_count[song_instance.genre] += 1
        else:
            cls.genre_count[song_instance.genre] = 1

    @classmethod
    def add_to_artist_count(cls, song_instance):
        if cls.artist_count.get(song_instance.artist):  # If the artist is already in the dictionary
            cls.artist_count[song_instance.artist] += 1
        else:
            cls.artist_count[song_instance.artist] = 1
