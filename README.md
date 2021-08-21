# SpotiChecker

Check for unavaliable songs in your "Loved Tracks" playlist

> Note: This script was made for your own needs and
> there is a chance that this work will not develop over time

## How to setup this script

1. Go to [Spotify Developers Dashboard](https://developer.spotify.com/dashboard) page and create an app
2. Open app settings and copy the CLIENT_ID and CLIENT_SECRET and set this in code
3. Press "Edit settings" and set the redirect uri to http://localhost:8080


## How to use this script

1. Paste the CLIENT_ID and CLIENT_SECRET in the code
2. Open terminal and run `python main.py`
3. Login to Spotify in opened browser window *(No data is transferred to third parties)*
4. Wait until script check all your loved tracks *(This process can be long depending on "Loved Tracks" length)*
5. After check, you will see all unavailable tracks names and position in your "Loved Tracks" playlist *(Or you will see message that all tracks is available)*

## Credits

This script is using [spotipy](https://github.com/plamere/spotipy) library to communicate with Spotify API
