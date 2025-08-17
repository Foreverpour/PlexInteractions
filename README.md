\# Plex Playlist Exporter (M3U)



This Python script connects to your Plex server and exports a specified playlist to an `.m3u` file for use with DLNA/HEOS or other media players.



\## Features

\- Connects via Plex API

\- Exports track metadata and file paths

\- Supports M3U format with `#EXTINF` tags



\## Usage

Update `PLEX\_URL`, `PLEX\_TOKEN`, and `PLAYLIST\_NAME` in the script, then run:



```bash

python export\_plex\_playlist.py

