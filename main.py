import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ID",
                                               client_secret="SECRET",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read"))


def check_loved_tracks_unavailability():
    offset_counter = 0
    unavailable_tracks = 0
    print('Checking your "Loved Tracks"...')
    start_time = time.perf_counter()
    tracks = sp.current_user_saved_tracks(limit=50)
    while tracks['items']:
        for i, item in enumerate(tracks['items']):
            track = sp.track(item['track']['id'], market='from_token')
            track_name = f"\'{track['artists'][0]['name']} - {track['name']}\'"
            track_pos = f"[{(i + 1) + offset_counter}]"
            if track['is_playable'] is False:
                unavailable_tracks += 1
                print(f"{track_pos} Track {track_name} is unavailable in your country")
        offset_counter += len(tracks['items'])
        tracks = sp.current_user_saved_tracks(limit=50, offset=offset_counter)
    stop_time = time.perf_counter()
    final_time = stop_time - start_time
    if unavailable_tracks == 0:
        print(f"All ({offset_counter}) tracks are available for listening!")
    else:
        print(f"{unavailable_tracks} track(s) out of {offset_counter} track(s) are unavilable!")
    print(f'Your "Loved Tracks" checked for {final_time} seconds')


if __name__ == '__main__':
    check_loved_tracks_unavailability()
