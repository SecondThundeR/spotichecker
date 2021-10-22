"""Utils for logging to Spotify.

This module contains functions for connecting to Spotify API.

This file can also be imported as a module and contains the following functions:
    * login_to_spotify - connect to Spotify and return OAuth object
"""


import spotipy
from spotipy.oauth2 import SpotifyOAuth


SCOPES = "user-library-read, playlist-read-private, playlist-read-collaborative"


def login_to_spotify(credentials: dict) -> SpotifyOAuth:
    """Trigger Spotify authentication and return current token.

    Args:
        credentials (dict): Credentials data (CLIENT_ID and CLIENT_SECRET).

    Returns:
        spotipy.oauth2.SpotifyOAuth: Spotify OAuth object.
    """
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=credentials["CLIENT_ID"],
        client_secret=credentials["CLIENT_SECRET"],
        redirect_uri="http://localhost:8080",
        scope=SCOPES
    ))
    return sp
