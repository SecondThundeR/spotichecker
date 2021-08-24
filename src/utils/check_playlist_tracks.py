"""Utils for checking certain playlist's unavailable tracks

This module contains functions for checking certain playlist's
unavailable tracks by its ID.

This file can also be imported as a module and contains the following functions:
    * check_playlist_tracks - runs all needed functions to check a playlist
"""

import time

from spotipy.exceptions import SpotifyException


def __get_playlist_name(sp_token, playlist_id):
    """Fetch playlist by ID and return its name.

    This function uses try/catch to check if playlist exists
    before executing playlist checking.

    Args:
        sp_token: Current active Spotify token
        playlist_id: ID of the playlist to check

    Returns:
        str: Name of the playlist
        None: If playlist does not exist
    """
    try:
        playlist_name = sp_token.playlist(playlist_id,
                                          fields=["name"],
                                          market="from_token")
    except SpotifyException:
        print("[Info] Unfortunately, something went wrong, exiting check...")
        return None
    return playlist_name["name"]


def __get_playlist_tracks(sp_token, playlist_id, offset):
    """Get 100 tracks with offset and returns them.

    This function calls for `playlist_items` method with
    certain fields which returns only tracks IDs and is_playable state.

    Args:
        sp_token: Current active Spotify token
        playlist_id: ID of the playlist to check
        offset: Offset of the tracks to get

    Returns:
        dict: Fetched playlist tracks
    """
    playlist_tracks = sp_token.playlist_items(
        playlist_id,
        limit=100,
        offset=offset,
        fields="items.track.id, items.track.name, "
        "items.track.artists, items.track.is_playable",
        market="from_token",
    )
    return playlist_tracks


def __check_for_unavailable_songs(sp_token, playlist_id):
    """Get playlist tracks and check for unavailable.

    Args:
        sp_token: Current active Spotify token
        playlist_id: ID of the playlist to check

    Returns:
        dict: Unavailable tracks info
        (Tracks count, Unavailable tracks count, Unavailable tracks dict)
    """
    offset_counter = 0
    unavailable_tracks_counter = 0
    unavailable_tracks_dict = {}
    playlist_tracks = __get_playlist_tracks(sp_token, playlist_id,
                                            offset_counter)
    while playlist_tracks["items"]:
        for i, item in enumerate(playlist_tracks["items"]):
            if item["track"]["is_playable"] is False:
                unavailable_tracks_counter += 1
                track_info = item["track"]
                track_name = (f"'{track_info['artists'][0]['name']} "
                              f"- {track_info['name']}'")
                track_pos = f"{(i + 1) + offset_counter}"
                unavailable_tracks_dict[track_pos] = track_name
        offset_counter += len(playlist_tracks["items"])
        print(f"Processed {offset_counter} song(s)...", end="\r")
        playlist_tracks = __get_playlist_tracks(sp_token, playlist_id,
                                                offset_counter)
    return {
        "tracks_count": offset_counter,
        "un_count": unavailable_tracks_counter,
        "un_tracks": unavailable_tracks_dict,
    }


def __print_check_details(tracks_info):
    """Get info from check and print summary of it.

    Args:
        sp_token: Current active Spotify token
        tracks_info: Dictionary with track info
    """
    tracks_count = tracks_info["tracks_count"]
    un_count = tracks_info["un_count"]
    if un_count == 0:
        print(f"All ({tracks_count}) tracks are available for listening!")
        return
    print(
        f"{un_count} track(s) out of {tracks_count} track(s) are unavilable!")
    print("\nHere are all list of unavailable songs:")
    for pos, name in tracks_info["un_tracks"].items():
        print(f"[{pos}] Track {name} is unavailable in your country")
    return


def check_playlist_tracks(sp_token, playlist_id):
    """Run all needed functions to check a playlist.

    This function also handles calculating time of the check
    and prints it after check summary.

    Args:
        sp_token: Current active Spotify token
        playlist_id: ID of the playlist to check
    """
    playlist_name = __get_playlist_name(sp_token, playlist_id)
    if playlist_name is None:
        return
    print(f'Processing "{playlist_name}" playlist...')
    start_time = time.perf_counter()
    un_tracks_info = __check_for_unavailable_songs(sp_token, playlist_id)
    stop_time = time.perf_counter()
    final_time = stop_time - start_time
    __print_check_details(un_tracks_info)
    print(f'\n"{playlist_name}" checked for {final_time} seconds')
