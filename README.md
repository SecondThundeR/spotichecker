# SpotiChecker

Check for unavaliable songs in your "Loved Tracks" playlist or any other playlist

> Note: This script was made for my own needs and
> there is a chance that this work will not develop over time and can be abandoned

## How to use this script

### Prepare Stage

1. Go to [Spotify Developers Dashboard](https://developer.spotify.com/dashboard) page and create an app
2. Open app settings and copy the CLIENT_ID and CLIENT_SECRET and copy it somewhere
3. Press "Edit settings" and set the redirect uri to http://localhost:8080
4. Make sure you have installed Python 3.x
5. If you are using Pipenv, run `pipenv shell && pipenv install`. Otherwise run `pip install spotipy`

### Main Stage

1. Run `python main.py`
2. Paste your `CLIENT_ID` and `CLIENT_SECRET` to store them and use later on
3. Login to Spotify in opened browser window *(No credentials is transferred to third parties)*
4. Choose required option in menu *(This process can be long depending on "Loved Tracks" or choosen playlist size)*
5. After check, you will see all unavailable tracks names and position in your "Loved Tracks" or choosen playlist *(Otherwise you will see message that all tracks are available)*

> This script will only tell you that some song or songs are unavailable in your country *(Depending on country from your Spotify Access Token)*. To check where **album** of song is available, use [albums-availability](https://kaaes.github.io/albums-availability/) app by [kaaes](https://github.com/kaaes) *(Check brief description on [Spotify Developers](https://developer.spotify.com/community/showcase/album-availability/) page)*

## Credits

This script is using [spotipy](https://github.com/plamere/spotipy) library to communicate with Spotify API
