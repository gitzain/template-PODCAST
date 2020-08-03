import eyed3
track = eyed3.load("test.mp3")
print(track.tag.album)