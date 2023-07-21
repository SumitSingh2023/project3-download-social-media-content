from pytube import YouTube
link=input("enter the url: ")
yt=YouTube(link)
stream=yt.streams.get_highest_resolution()
stream.download()
print("done")