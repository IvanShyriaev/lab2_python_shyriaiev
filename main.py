import track
import playlist
import album
import chart
import time

track1 = track.Track("15 step", 'Radiohead', 'In Rainbows', 2007, 240, 1_000_000, 8.9)
track2 = track.Track('Step on me', 'The cardigans', 'First band on the moon', 1996, 240, 5_000_000, 8.2)
track3 = track.Track("Jigsaw falling into place", 'Radiohead', 'In Rainbows', 2007, 275, 9_000_000, 9.5)
track4 = track.Track("Iron lung", "KG&LW", "Ice, Death, Planets, Lungs, Mushrooms and Lava", 2022, 546, 3_000_000, 8.6)

print(track1)
print("Score track2:",track2.score)
track2.score = 7.9
print("new score: ",track2.score)
track1.play()
time.sleep(1)
track1.stop()

playlist1 = playlist.Playlist([ track2, track4, track1], "My Music", "Ivan Shyriaiev")
print('\n',playlist1)
print("Duration: ",playlist1.duration())
print("tracks in playlist1: ",playlist1.count_tracks())
playlist.Playlist.remove_track(playlist1, '15 step')
print(playlist1)

album1 = album.Album([track1, track3], 'In rainbows', 'Radiohead', 2007)
print("\n",album1)
print("Tracks in album:", album1.count_tracks())
album1.play()
time.sleep(1)
album1.stop()

chart1 = chart.Chart([track1, track3, track4])
print('\n')
chart1.find_track('15 step')
print('\n', chart1)
chart1.add_track(track2)

chart1.print_chart()