from pytube import YouTube

def download_video(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
        print("Download completed successfully")
    except:
        print("An error has occurred")

link = input("Enter the YouTube video URL: ")
download_video(link)
