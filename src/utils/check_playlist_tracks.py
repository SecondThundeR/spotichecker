"""Utils for checking certain playlist's unavailable tracks.

This module contains functions for checking certain playlist's
unavailable tracks by its ID.

This file can also be imported as a module and contains the following functions:
    * check_playlist_tracks - runs all needed functions to check a playlist
"""


import time

from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException


def __get_playlist_name(sp: SpotifyOAuth, playlist_id: str) -> str | None:
    """Fetch playlist by ID and return its name.

    This function uses try/catch to check if playlist exists
    before executing playlist checking.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.
        playlist_id (str): ID of the playlist to check

    Returns:
        str: Name of the playlist
        None: If playlist does not exist
    """
    try:
        playlist_name = sp.playlist(
            playlist_id,
            fields=["name"],
            market="from_token"
        )["name"]
    except SpotifyException:
        print("[Info] Unfortunately, something went wrong, exiting check...\n")
        return None
    return playlist_name


def __check_for_unavailable_songs(sp: SpotifyOAuth, playlist_id: str) -> dict:
    """Get playlist tracks and check for unavailable.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.
        playlist_id (str): ID of the playlist to check

    Returns:
        dict: Unavailable tracks info
        (Tracks count, Unavailable tracks count, Unavailable tracks dict)
    """
    offset_counter = 0
    unavailable_tracks_counter = 0
    local_tracks = 0
    unavailable_tracks_dict = {}
    playlist_tracks = sp.playlist_items(
        playlist_id,
        limit=100,
        fields="items.track.id, items.track.name, "
        "items.track.artists, items.track.is_playable, next",
        market="from_token",
    )
    while playlist_tracks is not None:
        for index, item in enumerate(playlist_tracks["items"]):
            try:
                if item["track"]["is_playable"] is False:
                    unavailable_tracks_counter += 1
                    track_info = item["track"]
                    track_name = (
                        f"'{track_info['artists'][0]['name']} "
                        f"- {track_info['name']}'"
                    )
                    track_pos = f"{(index + 1) + offset_counter}"
                    unavailable_tracks_dict[track_pos] = track_name
            except KeyError:
                if item["track"]["is_local"]:
                    local_tracks += 1
        offset_counter += len(playlist_tracks["items"])
        print(f"[Info] Processed {offset_counter} song(s)...", end="\r")
        playlist_tracks = sp.next(playlist_tracks)
    return {
        "tracks_count": offset_counter,
        "un_count": unavailable_tracks_counter,
        "un_tracks": unavailable_tracks_dict,
        "local_count": local_tracks,
    }


def __print_check_details(playlist_name: str, tracks_info: dict) -> None:
    """Get info from check and print summary of it.

    Args:
        playlist_name (str): Name of checked playlist
        tracks_info (dict): Dictionary with track info
    """
    tracks_count = tracks_info["tracks_count"]
    un_count = tracks_info["un_count"]
    local_count = tracks_info["local_count"]
    non_local_count = tracks_count - local_count
    print("\n\n======== Check summary ========")
    if un_count == 0:
        if local_count == 0:
            print(
                f'All ({tracks_count}) tracks are available for listening in "{playlist_name}"!'
            )
            print("===============================")
            return
        print(
            f'All ({non_local_count}) tracks are available for listening in "{playlist_name}"!'
        )
        print(f"[Note] Ignored {local_count} local track(s)")
        print("===============================")
        return
    if local_count > 0:
        print(
            f'{un_count} out of {non_local_count} track(s) are unavailable in "{playlist_name}"!'
        )
        print(f"[Note] Ignored {local_count} local track(s)")
        print("===============================")
    else:
        print(
            f'{un_count} out of {tracks_count} track(s) are unavailable in "{playlist_name}"!'
        )
    print("\nHere are all list of unavailable songs:")
    for pos, name in tracks_info["un_tracks"].items():
        print(f"[{pos}] Track {name} is unavailable in your country")
    print("===============================")
    return


def check_playlist_tracks(sp: SpotifyOAuth, playlist_id: str) -> None:
    """Run all needed functions to check a playlist.

    This function also handles calculating time of the check
    and prints it after check summary.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object
        playlist_id (str): ID of the playlist to check
    """
    playlist_name = __get_playlist_name(sp, playlist_id)
    if playlist_name is None:
        return
    print(f"\n[Info] Chosen {playlist_name} playlist!")
    print("[Info] Processing playlist...", end="\r")
    start_time = time.perf_counter()
    un_tracks_info = __check_for_unavailable_songs(sp, playlist_id)
    stop_time = time.perf_counter()
    final_time = stop_time - start_time
    __print_check_details(playlist_name, un_tracks_info)
    print(f"\n[Info] Playlist checked for {final_time} seconds")
    input("Press any button to continue...\n")
