"""SpotiChecker.

This is a Python script that uses Spotify API to check for unavailable
tracks in "Loved Tracks" section or choosen playlist.
"""


import os
import sys
import configparser

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from src.utils.check_loved_tracks import check_loved_tracks
from src.utils.check_playlist_tracks import check_playlist_tracks
from src.utils.credentials_manager import initial_configuration
from src.utils.get_users_playlists import get_users_playlists


SCOPES = "user-library-read, playlist-read-private, playlist-read-collaborative"


def credentials_checker() -> dict:
    """Check if credentials file.

    If credentials file doesn't exist, run initial setup to
    create a new credentials file.

    Returns:
        dict: Dictionary with CLIENT_ID and CLIENT_SECRET
    """
    if os.path.isfile("spotichecker.ini"):
        config = configparser.ConfigParser()
        config.read("spotichecker.ini")
        return {
            "CLIENT_ID": config["CREDENTIALS"]["CLIENT_ID"],
            "CLIENT_SECRET": config["CREDENTIALS"]["CLIENT_SECRET"]
        }
    else:
        credentials_data = initial_configuration()
        return credentials_data


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


def main_menu(sp: SpotifyOAuth) -> None:
    """Print main menu.

    This function handles printing available options and getting
    input from user to run certain check functions.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
    """
    print("=== Welcome to SpotiChecker! ===\n")
    while True:
        print("========= Menu Options =========")
        print("Choose option to continue:")
        print('1. Check your "Loved Tracks"')
        print("2. Check your created playlists")
        print("3. Check playlist by ID")
        print("0. Exit")
        try:
            option = int(input("> "))
        except ValueError:
            print("[Error] You entered something other than the number. Try again\n")
            continue
        if option == 1:
            check_loved_tracks(sp)
        elif option == 2:
            get_users_playlists(sp)
        elif option == 3:
            playlist_id = input("\nEnter playlist ID: ")
            check_playlist_tracks(sp, playlist_id)
        elif option == 0:
            print("=== See you soon! ===")
            sys.exit()
        else:
            print("[Error] You entered wrong option number. Try again\n")
            continue


if __name__ == "__main__":
    credits_data = credentials_checker()
    spotify_oauth = login_to_spotify(credits_data)
    main_menu(spotify_oauth)
