import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.utils.check_loved_tracks import check_loved_tracks


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ID",
                                               client_secret="SECRET",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read"))


if __name__ == '__main__':
    check_loved_tracks()
