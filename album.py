from track import Track
from playlist import Playlist

class Album(Playlist, Track):
    def __init__(self, tracks, name, author, year_of_release):
        Playlist.__init__(self, tracks, name, author)
        self.year_of_release = year_of_release
        self.is_playing = False
        self._start_time = None
        self._elapsed_time = 0