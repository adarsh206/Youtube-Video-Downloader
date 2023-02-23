#   *****  If want to download playlist(all video at a time of a folder/directory)  *****

from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list=PL-osiE80TeTsKOdPrKeSOp4rN3mza8VHN")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()


print(" Successfully Downloaded ")