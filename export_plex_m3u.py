from plexapi.server import PlexServer

# 🔐 Plex credentials
PLEX_URL = 'http://192.168.50.251:32400'
PLEX_TOKEN = 'R6_v4Ez82AVcbnWuUe1T'

# 🎵 Playlist name and export path
PLAYLIST_NAME = 'Essentials'
EXPORT_PATH = 'Essentials.m3u'

# 🔌 Connect to Plex
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# 🔍 Find the playlist
playlist = next((pl for pl in plex.playlists() if pl.title == PLAYLIST_NAME), None)

if not playlist:
    print(f"Playlist '{PLAYLIST_NAME}' not found.")
    exit()

# 🧾 Write M3U file
with open(EXPORT_PATH, 'w', encoding='utf-8') as m3u:
    m3u.write("#EXTM3U\n")
    for item in playlist.items():
        if item.TYPE == 'track':
            duration_sec = item.duration // 1000 if item.duration else -1
            artist = item.originalTitle or item.grandparentTitle or 'Unknown Artist'
            title = item.title or 'Unknown Title'
            try:
                file_path = item.media[0].parts[0].file
                m3u.write(f"#EXTINF:{duration_sec},{artist} - {title}\n")
                m3u.write(f"{file_path}\n")
            except Exception as e:
                print(f"⚠️ Skipped track due to missing file path: {title} by {artist}")

print(f"✅ Exported {len(playlist.items())} tracks to {EXPORT_PATH}")