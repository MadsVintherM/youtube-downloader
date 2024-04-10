from pytube import YouTube
from sys import argv

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = bytes_downloaded / total_size * 100
    print('\r', 'Downloading: {:.2f}%'.format(percentage_of_completion), end='')


if len(argv) > 1:
    link = argv[1]
    yt = YouTube(link)

    
    yt.register_on_progress_callback(progress_function)

    print("Title:", yt.title)
    print("Number of views:", yt.views)

    yd = yt.streams.get_highest_resolution()
    print("Downloading...")
    yd.download('/Users/Name/Desktop/youtube-downloader')
    print("\nDownload completed!")
else:
    print("Please provide a YouTube link as an argument.")
