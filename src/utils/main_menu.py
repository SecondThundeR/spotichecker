"""Utils for main menu.

This module contains functions for initializing main menu.

This file can also be imported as a module and contains the following functions:
    * main_menu - print main menu
"""


import sys


from src.utils.check_loved_tracks import check_loved_tracks
from src.utils.check_playlist_tracks import check_playlist_tracks
from src.utils.credentials_manager import credentials_checker
from src.utils.get_users_playlists import get_users_playlists
from src.utils.login_to_spotify import login_to_spotify


def main_menu() -> None:
    """Print main menu.

    This function handles printing available options and getting
    input from user to run certain check functions.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
    """

    credits_data = credentials_checker()
    spotify_oauth = login_to_spotify(credits_data)

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
            check_loved_tracks(spotify_oauth)
        elif option == 2:
            get_users_playlists(spotify_oauth)
        elif option == 3:
            playlist_id = input("\nEnter playlist ID: ")
            check_playlist_tracks(spotify_oauth, playlist_id)
        elif option == 0:
            print("=== See you soon! ===")
            sys.exit()
        else:
            print("[Error] You entered wrong option number. Try again\n")
            continue
