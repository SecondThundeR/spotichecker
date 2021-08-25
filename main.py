"""SpotiChecker.

This is a Python script that uses Spotify API to check for unavailable
tracks in "Loved Tracks" section or choosen playlist.
"""

import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from src.utils.check_loved_tracks import check_loved_tracks
from src.utils.check_playlist_tracks import check_playlist_tracks
from src.utils.get_users_playlists import get_users_playlists


def login_to_spotify():
    """Trigger Spotify authentication and return current token.

    Returns:
        spotipy.oauth2.SpotifyOAuth: Spotify OAuth object.
    """
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="ID",
        client_secret="SECRET",
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
    spotify_oauth = login_to_spotify()
    main_menu(spotify_oauth)
