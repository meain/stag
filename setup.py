import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

cur_classifiers = [
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Multimedia :: Sound/Audio :: Editors",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Operating System :: POSIX",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: MIT License",
]

install_requires = ["eyed3", "spotipy"]

setuptools.setup(
    name="pystag",
    version="0.0.5",
    author="Abin Simon",
    author_email="abinsimon10@gmail.com",
    description="Tag local music using spotify api",
    url="https://github.com/meain/stag",
    long_description=long_description,
    packages=["stag"],
    keywords=["spotify", "music", "tagging"],
    classifiers=cur_classifiers,
    entry_points={"console_scripts": ["stag = stag.stag:main"]},
)
