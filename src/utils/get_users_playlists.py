"""Utils for getting user's playlists.

This module contains functions for getting and
parsing user's playlists.

This file can also be imported as a module and contains the following functions:
    * get_users_playlists() - gets and prints user's playlists.
"""


import time

from spotipy.oauth2 import SpotifyOAuth

from src.utils.check_playlist_tracks import check_playlist_tracks


def __fetch_users_playlists(sp: SpotifyOAuth) -> None:
    """Get all user's playlists and return only created ones

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
    """
    username = sp.me()["display_name"]
    user_playlists = {}
    user_playlists_counter = 0
    playlists_counter = 0
    playlists = sp.user_playlists(username)
    while playlists is not None:
        for playlist in playlists["items"]:
            if playlist['owner']['display_name'] == username:
                user_playlists[user_playlists_counter + 1] = playlist
                user_playlists_counter += 1
        playlists_counter += len(playlists["items"])
        print(f"[Info] Processed {playlists_counter} playlist(s)...", end="\r")
        playlists = sp.next(playlists)
    return {
        "playlists": user_playlists,
        "playlists_count": user_playlists_counter
    }

def __print_check_details(playlists: dict, time: float) -> None:
    """Get info from check and print summary of it.

    Args:
        playlists (dict): Playlists, owned by user
        time (float): Elapsed time on checking
    """
    print("\n\n======== Check summary ========")
    if playlists['playlists_count'] == 0:
        print("There are no playlists owned by you")
        print(f"All playlists checked in {time} seconds!")
        print("===============================")
        return
    print(f"Found {playlists['playlists_count']} playlist(s) owned by you in {time} seconds!\n\nHere are your playlists:")
    for index, playlist in playlists["playlists"].items():
        print(f"{index}. {playlist['name']}")
    print("===============================")


def __select_playlist_to_check(sp: SpotifyOAuth, playlists: dict) -> None:
    """Give user choice to select playlist for checking.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
        playlists (dict): Playlists, owned by user
    """
    print("\nWhat playlist do you want to open? (Tip: Enter index of the playlist)")
    while True:
        chosen_playlist_index = input("> ")
        if chosen_playlist_index == "":
            print("\n[Error] You have not entered anything, "
                  "enter index of the playlist to continue")
            continue
        try:
            chosen_playlist = playlists[int(chosen_playlist_index)]
            break
        except KeyError:
            print("\n[Error] You entered the wrong index of the playlist, "
                  "enter correct index of the playlist to continue")
            continue
    check_playlist_tracks(sp, chosen_playlist['id'])


def get_users_playlists(sp: SpotifyOAuth) -> None:
    """Get and print playlists, created by user.

    This function gets user's playlists and prints them.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
    """
    print(f"\n[Info] Processing user's playlist...")
    start_time = time.perf_counter()
    user_playlists = __fetch_users_playlists(sp)
    stop_time = time.perf_counter()
    final_time = stop_time - start_time
    __print_check_details(user_playlists, final_time)
    if len(user_playlists["playlists"]) > 0:
        __select_playlist_to_check(sp, user_playlists["playlists"])
    else:
        input("Press any button to continue...\n")
