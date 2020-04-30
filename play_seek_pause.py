from rtmidi.midiutil import open_midiinput

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import time
import os

class MidiInputHandler(object):
    def __init__(self, port, freq):
        self.port = port
        self.base_freq = freq
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        global currentFrequency
        message, deltatime = event
        self._wallclock += deltatime
        print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))
        if (message[1] == 41) and (message[2] == 127):
            try:
                sp.start_playback()
            except Exception as e:
                print(e)
        if (message[1] == 43) and (message[2] == 127):
            try:
                sp.seek_track(0)
            except Exception as e:
                print(e)
        if (message[1] == 42) and (message[2] == 127):
            try:
                sp.pause_playback()
            except Exception as e:
                print(e)

client_credentials_manager = SpotifyClientCredentials()

# assumes we've set environment variables for SPOTIFY_OAUTH_TOKEN,
# SPOTIPY_CLIENT_SECRET, and SPOTIPY_CLIENT_ID
sp = spotipy.Spotify(auth=os.environ['SPOTIFY_OAUTH_TOKEN'],
                     client_credentials_manager=client_credentials_manager)

try:
    midiin, port_name = open_midiinput(0)
except (EOFError, KeyboardInterrupt):
    exit()

midiSettings = MidiInputHandler(port_name, 940.0)
midiin.set_callback(midiSettings)


while True:
    time.sleep(.1)

