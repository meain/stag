# stag

**Spotify tagger**

Tag your local music using spotify api.

![gif](https://i.imgur.com/5uYTIyJ.gif)

> Adds proper `title`, `album` and `artist` and renames file to `title`.

## Requirements

- `eyed3` ( tag songs )
- `spotipy` ( spotify api client )

## Usage

You need to set 3 environment variables for `stag`

- `SPOTIFY_CLIENT_ID`
- `SPOTIFY_CLIENT_SECRET`
- `SPOTIFY_USERNAME`

Once this is set you can just run: `python3 stag.py`
