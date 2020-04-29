from rtmidi.midiutil import open_midiinput

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from time import sleep
import os

client_credentials_manager = SpotifyClientCredentials()

# assumes we've set environment variables for SPOTIFY_OAUTH_TOKEN,
# SPOTIPY_CLIENT_SECRET, and SPOTIPY_CLIENT_ID
sp = spotipy.Spotify(auth=os.environ['SPOTIFY_OAUTH_TOKEN'],
                     client_credentials_manager=client_credentials_manager)

sp.start_playback()
sleep(10)
sp.seek_track(0)
sleep(10)
sp.pause_playback()
import IPython
IPython.embed()
