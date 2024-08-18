import yt_dlp
from moviepy.editor import AudioFileClip
import os

def download_video(youtube_url, output_path='/path/to/mp3/'):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Download the video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def main():
    youtube_url = input('Enter the YouTube video URL: ')
    download_video(youtube_url)
    print('Video downloaded and converted to MP3.')

if __name__ == '__main__':
    main()

