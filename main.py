"""SpotiChecker.

This is a Python script that uses Spotify API to check for unavailable
tracks in "Loved Tracks" section or choosen playlist.
"""

import configparser
import os
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from src.utils.check_loved_tracks import check_loved_tracks
from src.utils.check_playlist_tracks import check_playlist_tracks
from src.utils.credentials_manager import initial_configuration
from src.utils.get_users_playlists import get_users_playlists



def credentials_checker():
    """Check if credentials file.

    If credentials file doesn't exist, run initial setup to
    create a new credentials file.
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


def login_to_spotify(credentials):
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
        scope="user-library-read",
    ))
    return sp


def main_menu(sp):
    """Print main menu.

    This function handles printing available options and getting
    input from user to run certain check functions.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.
    """
    print("Welcome to SpotiChecker!\n")
    while True:
        print("Choose option to continue:")
        print('1. Check your "Loved Tracks"')
        print("2. Check playlist by ID")
        print("3. Check playlist on your account")
        print("0. Exit")
        try:
            option = int(input("> "))
        except ValueError:
            print("You entered something wrong. Try again\n")
            continue
        if option == 1:
            check_loved_tracks(sp)
        elif option == 2:
            playlist_id = input("\nEnter playlist ID: ")
            check_playlist_tracks(sp, playlist_id)
        elif option == 3:
            print("\n[Info] This feature currently not implemented!\n")
            # get_users_playlists(sp)
        elif option == 0:
            print("See you soon!")
            sys.exit()


if __name__ == "__main__":
    credits_data = credentials_checker()
    spotify_oauth = login_to_spotify(credits_data)
    main_menu(spotify_oauth)
