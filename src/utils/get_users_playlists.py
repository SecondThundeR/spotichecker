def get_users_playlists(sp):
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
