from pytube import YouTube

link = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
#audio = youtube_1.streams.filter(only_audio=True)   # if you want to download only audio format

videos = youtube_1.streams.all()      # All format
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input(" Enter : "))
videos[strm].download()
print(" Successfully Downloaded ")    