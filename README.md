# SpotiChecker

Check for unavaliable songs in your "Loved Tracks" playlist or any other playlist

> Note: This script was made for my own needs and
> there is a chance that this work will not develop over time and can be abandoned

## How to setup this script

1. Go to [Spotify Developers Dashboard](https://developer.spotify.com/dashboard) page and create an app
2. Open app settings and copy the CLIENT_ID and CLIENT_SECRET and set this in code
3. Press "Edit settings" and set the redirect uri to http://localhost:8080


## How to use this script

0. Make sure you have installed Python 3.x
1. Open terminal and run `python main.py`
2. On first run, script will ask you to paste your `CLIENT_ID` and `CLIENT_SECRET` to store them and use later on
3. Then, login to Spotify in opened browser window *(No data is transferred to third parties)*
4. Choose needed option in text menu *(This process can be long depending on "Loved Tracks"/Choosen playlist length)*
5. After check, you will see all unavailable tracks names and position in your "Loved Tracks"/Choosen playlist *(Or you will see message that all tracks are available)*

> This script will only tell you that some song or songs are unavailable in your country *(Depending on country from your Spotify Access Token)*. To check where album of song is available, use [albums-availability](https://kaaes.github.io/albums-availability/) app by [kaaes](https://github.com/kaaes) *(Check brief description on [Spotify Developers](https://developer.spotify.com/community/showcase/album-availability/) page)*

## Credits

This script is using [spotipy](https://github.com/plamere/spotipy) library to communicate with Spotify API
