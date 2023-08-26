class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    @classmethod
    def add_song_to_count(self):
        Song.count += 1

    @classmethod
    def add_to_genres(self, genre):
        if(genre not in Song.genres):
            Song.genres.append(genre)

    @classmethod
    def add_to_artists(self, artist):
        if(artist not in Song.artists):
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(self, genre):
        

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
