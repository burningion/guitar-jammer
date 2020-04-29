# Guitar Jammer

Connect to the Spotify API and control the playback of music with your feet so you can jam

## How this (will) work

It doesn't. Yet. For now, here are the relevant API calls I'm going to use (note, setting up the proper login flow is a PITA on Spotify, and `spotipy` exists, but for now just going off my own OAuth API key I'll generate manually):


**Play / Resume:**

```
$ curl -X "PUT" "https://api.spotify.com/v1/me/player/play" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer  "
```

**Pause**

```
$ curl -X "PUT" "https://api.spotify.com/v1/me/player/pause" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "
```

**Seek to Point**

```
$ curl -X "PUT" "https://api.spotify.com/v1/me/player/seek?position_ms=500" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "
```

It seems like the easiest thing to begin with is playing a song, adding a seek to point at the beginning, having a timer, and adding two buttons to do either go back 5 seconds, restart the song, pause, or play. 

Maybe add another button to record audio of searching for a new track to play.
