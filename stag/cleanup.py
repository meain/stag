import os
import re
import glob

files = glob.glob("./*.mp3")


def multi_dash_cleanup(string):
    chunks = re.split(r"[-|_|–]", string)
    if len(chunks) > 2:
        return "-".join(chunks[:2]).strip()
    return "-".join(chunks)


def get_clean_name(f):
    fn = re.sub(r"[\(\[].*[\)\]]", "", f)
    fn = multi_dash_cleanup(fn)
    return fn


def main():
    for f in files:
        fn = re.sub(r"[\(\[].*[\)\]]", "", f)
        fn = multi_dash_cleanup(fn)
        if not fn.endswith(".mp3"):
            fn = fn + ".mp3"
        os.rename(f, fn)


if __name__ == "__main__":
    main()
