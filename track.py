import time

class Track:
    def __init__(self, name, author, album, year_of_release, duration, listens, score):
        self.name = name
        self.author = author
        self.album = album
        self.year_of_release = year_of_release
        self.duration = duration
        self._listens = listens
        self._score = score
        self.is_playing = False
        self._start_time = None
        self._elapsed_time = 0

    def __str__(self):
        return f'{self.name} by {self.author}, from album {self.album}, {self.year_of_release}, {self.duration} seconds'

    def play(self):
        if not self.is_playing:
            self._start_time = time.time()
            self.is_playing = True
            print(f"Playing {self.name} by {self.author}")

    def stop(self):
        if self.is_playing:
            self._elapsed_time += time.time() - self._start_time
        self.is_playing = False
        print(f"Stopped {self.name} after {self._elapsed_time:.0f} seconds")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0 or value > 10:
            raise ValueError("Score must be between 0 and 10")
        self._score = value

    @property
    def listens(self):
        return self._listens

    @listens.setter
    def listens(self, value):
        if value < 0:
            raise ValueError("Listen must be more than 0")
        self._listens = value