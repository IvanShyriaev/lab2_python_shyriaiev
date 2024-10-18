from playlist import Playlist


def sort_tracks(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.tracks.sort(key=lambda track: (track.score ** track.score) * track.listens, reverse=True)
        return result
    return wrapper

class Chart(Playlist):
    def __init__(self, tracks, name='Chart', author='None'):
        super().__init__(tracks, name, author)
        self.tracks = self.__make_chart()


    def __make_chart(self):
        return sorted(self.tracks, key=lambda track: (track.score ** track.score) * track.listens, reverse=True)

    def find_track(self, name):
        position = 1
        for track in self.tracks:
            if track.name == name:
                print(f'{track.name} by {track.author} is on {position} position')
            position += 1

    def print_chart(self):
        position = 1
        for track in self.tracks:
            print(f'{position}: {track.name} by {track.author}, score: {track.score}, listens: {track.listens}')
            position += 1

    @sort_tracks
    def add_track(self, track):
        super().add_track(track)

    @sort_tracks
    def remove_track(self, track_name):
        super().remove_track(track_name)