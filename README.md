# stag

**Spotify tagger**

Tag your local music using spotify api.

![gif](https://i.imgur.com/eoPL9xZ.gif)

> Adds proper `title`, `album`, `artist` and `album art` and renames file to `title`.


## Installation

```
pip3 install pystag
```

## Usage

You need to set 3 environment variables for `stag`

- `SPOTIFY_CLIENT_ID`
- `SPOTIFY_CLIENT_SECRET`
- `SPOTIFY_USERNAME`

Once this is set you can just run `stag` in the folder with the songs.

Go [here](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app) to know how to
generate a `CLIENT_ID` and `CLIENT_SECRET`. To get the `USERNAME` just check the profile share link in your profile.
Your profile share link will look something like `https://open.spotify.com/user/<USERNAME>?si=<SOMETHING_ELSE>`

## Requirements

- `eyed3` ( tag songs )
- `spotipy` ( spotify api client )
