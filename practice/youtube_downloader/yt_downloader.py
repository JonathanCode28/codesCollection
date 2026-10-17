from pytube import YouTube

#download function
def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully")
    except Exception as e:
        print("Error: ", str(e))

#get the video URL
video_url = input("Enter the YouTube video link: ")

#call the download_video func

download_video(video_url)