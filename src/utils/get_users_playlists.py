"""Utils for getting user's playlists.

This module contains functions for managing gettings and
parsing user's playlists.

This file can also be imported as a module and contains the following functions:
    * get_users_playlists() - gets and prints user's playlists.
"""


def get_users_playlists(sp):
    """Get and print playlists, created by user.

    This function gets user's playlists and prints them.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.
    """
    # TODO: Save playlist IDs to dict
    user_data = sp.me()
    playlists = sp.user_playlists(user_data["display_name"])
    while playlists:
        for i, playlist in enumerate(playlists["items"]):
            print(f"{i + 1}. {playlist['name']}")
        if playlists["next"]:
            playlists = sp.next(playlists)
        else:
            playlists = None
