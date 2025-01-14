import pytube

link = ("Paste Youtube URL here: ")

yt = pytube.YouTube(link)

yt.streams.first().download()

print("Video Downloaded!")

