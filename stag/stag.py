import sys
import re
import os
import glob
import eyed3
import spotipy

import spotipy.util
from spotipy.oauth2 import SpotifyClientCredentials

from .cleanup import get_clean_name

ERASE_LINE = "\x1b[2K"
CURSOR_UP_ONE = "\x1b[1A"
creds = {
    "clientId": os.environ["SPOTIFY_CLIENT_ID"],
    "clientSecret": os.environ["SPOTIFY_CLIENT_SECRET"],
    "username": os.environ["SPOTIFY_USERNAME"],
}


class colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    ENDC = "\033[0m"


def get_spotify_instace():

    access = "user-library-modify"
    redirectURL = "http://localhost/"
    token = spotipy.util.prompt_for_user_token(
        username=creds["username"],
        scope=access,
        client_id=creds["clientId"],
        client_secret=creds["clientSecret"],
        redirect_uri=redirectURL,
    )
    client_manager = SpotifyClientCredentials(creds["clientId"], creds["clientSecret"])
    sp = spotipy.Spotify(auth=token, client_credentials_manager=client_manager)
    return sp


sp = get_spotify_instace()


def get_song(name):
    results = sp.search(q=name, limit=1)
    if len(results["tracks"]["items"]) > 0:
        return results["tracks"]["items"][0]
    return False


def get_name(path: str) -> str:
    file_name = os.path.basename(path)
    song = re.sub(".mp3$", "", file_name)
    return song


def get_files(base="."):
    files = glob.glob(f"{base}/*.mp3")
    return files


def tag_song(path, info):
    audiofile = eyed3.load(path)
    audiofile.tag.artist = info["artists"][0]["name"]
    audiofile.tag.album = info["album"]["name"]
    audiofile.tag.title = info["name"]

    audiofile.tag.save()


def rename_file(path, info):
    from_path = path
    filename = get_name(path)
    to_path = path.replace(filename, info["name"])
    try:
        os.rename(from_path, to_path)
    except Exception:
        print("Could not rename", from_path)


def print_item(number, name, success=True, c_song=""):
    try:
        columns = int(os.popen("stty size", "r").read().split()[1])
    except Exception:
        columns = 100
    bar_len = min(150, columns - 10)
    name = name[:bar_len]
    if success:
        sys.stdout.write(ERASE_LINE)
        sys.stdout.write("%s: %s%s%s\r\n" % (number, colors.GREEN, name, colors.ENDC))
    else:
        sys.stdout.write(ERASE_LINE)
        sys.stdout.write(
            "%s: %s%s%s (%s)\r\n" % (number, colors.RED, name, colors.ENDC, c_song)
        )


def is_tagged(path):
    audiofile = eyed3.load(path)
    if (
        audiofile.tag.artist
        and len(audiofile.tag.artist) > 0
        and audiofile.tag.album
        and len(audiofile.tag.album) > 0
        and audiofile.tag.title
        and len(audiofile.tag.title) > 0
    ):
        return True
    return False


def main():
    files = get_files()
    print(f"Tagging {len(files)} songs")
    failed = []
    for i, f in enumerate(files):
        song = get_name(f)
        if is_tagged(f):
            print_item(i + 1, song)
            continue
        c_song = get_clean_name(get_name(f))
        info = get_song(c_song)
        if info:
            print_item(i + 1, song)
            tag_song(f, info)
            rename_file(f, info)
        else:
            failed.append(song)
            print_item(i + 1, song, False, c_song)

    # sys.stdout.write(ERASE_LINE)
    # sys.stdout.write(CURSOR_UP_ONE)
    # sys.stdout.write(ERASE_LINE)
    if len(failed) > 0:
        print(f"\nCould not fetch info for the following {len(failed)} song(s).")
        print("Try renaming them to simpler names.\n")
        for song in failed:
            print("-", song)
    else:
        pass  # no need with \r\n
        # print("Tagging complete")


if __name__ == "__main__":
    main()
