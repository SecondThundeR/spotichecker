"""Utils for checking user's "Loved Tracks" playlist for unavailable tracks.

This module contains functions for "Loved Tracks" playlist
for unavailable tracks.

This file can also be imported as a module and contains the following functions:
    * check_loved_tracks - runs all needed functions to check "Loved Tracks"
"""


import time


def __check_for_unavailable_songs(sp):
    """Get "Loved Tracks" and check for unavailable.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.

    Returns:
        dict: Unavailable tracks info
        (Tracks count, Unavailable tracks count, Unavailable tracks dict)
    """
    offset_counter = 0
    unavailable_tracks_counter = 0
    unavailable_tracks_dict = {}
    loved_tracks = sp.current_user_saved_tracks(limit=50)
    while loved_tracks is not None:
        tracks_id_list = []
        for item in loved_tracks["items"]:
            tracks_id_list.append(item["track"]["id"])
        checked_tracks = sp.tracks(tracks=tracks_id_list, market="from_token")
        for i, item in enumerate(checked_tracks["tracks"]):
            if item["is_playable"] is False:
                unavailable_tracks_counter += 1
                track_name = f"'{item['artists'][0]['name']} - {item['name']}'"
                track_pos = f"{(i + 1) + offset_counter}"
                unavailable_tracks_dict[track_pos] = track_name
        offset_counter += len(loved_tracks["items"])
        print(f"Processed {offset_counter} song(s)...", end="\r")
        loved_tracks = sp.next(loved_tracks)
    return {
        "tracks_count": offset_counter,
        "un_count": unavailable_tracks_counter,
        "un_tracks": unavailable_tracks_dict,
    }


def __print_check_details(tracks_info):
    """Get info from check and print summary of it.

    Because of the way "Loved Tracks" are checked, function for
    converting dictionary with IDs is not needed.

    Args:
        tracks_info: Dictionary with track info
    """
    tracks_count = tracks_info["tracks_count"]
    un_count = tracks_info["un_count"]
    if un_count == 0:
        print(f"All ({tracks_count}) tracks are available for listening!")
        return
    print(f"{un_count} track(s) out of {tracks_count} track(s) are unavilable!")
    print("\nHere are all list of unavailable songs:")
    for pos, name in tracks_info["un_tracks"].items():
        print(f"[{pos}] Track {name} is unavailable in your country")


def check_loved_tracks(sp):
    """Run all needed functions to check user's "Loved Tracks".

    This function also handles calculating time of the check
    and prints it after check summary.

    Args:
        sp (spotipy.oauth2.SpotifyOAuth): Spotify OAuth object.
    """
    print('\nProcessing your "Loved Tracks"...')
    start_time = time.perf_counter()
    un_tracks_info = __check_for_unavailable_songs(sp)
    stop_time = time.perf_counter()
    final_time = stop_time - start_time
    __print_check_details(un_tracks_info)
    print(f'\nYour "Loved Tracks" checked for {final_time} seconds')
    input("Press any button to continue...\n")
