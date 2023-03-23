from pytube import YouTube, Playlist

def get_info_stream(url):
    stream = {}
    if 'playlist' in url:
        playlist = Playlist(url)
        stream.update(
            {
                'title': playlist.title,
                'author': playlist.owner,
                'duration': f'{playlist.length} video(s)'
            }
        )
        
    else:
        yt = YouTube(url)
        stream.update(
            {
                'title': yt.title,
                'author': yt.author,
                'thumbnail': yt.thumbnail_url,
                'duration': f'{yt.length // 60}:{yt.length % 60} min'
            }
        )
    
    print(stream['thumbnail'])
        
    return stream
