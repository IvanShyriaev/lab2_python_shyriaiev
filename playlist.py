import track

class Playlist:
    def __init__(self, tracks, name, author):
        self.name = name
        self.author = author
        self.tracks = tracks

    def __str__(self):
        return f'{self.name} by {self.author}, {self.count_tracks()} tracks'

    def duration(self):
        return sum([track.duration for track in self.tracks])

    def add_track(self, track):
        self.tracks.append(track)

    @staticmethod
    def remove_track(playlist, track_name):
        for track in playlist.tracks:
            if track.name == track_name:
                playlist.tracks.remove(track)

    def count_tracks(self):
        return len(self.tracks)


