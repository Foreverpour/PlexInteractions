from plexapi.server import PlexServer

PLEX_URL = 'http://192.168.50.251:32400'  
PLEX_TOKEN = 'R6_v4Ez82AVcbnWuUe1T'         

def get_music_library_paths():
    try:
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        music_sections = [section for section in plex.library.sections() if section.type == 'artist']

        if not music_sections:
            print("😕 No music libraries found on your Plex server.")
            return

        print("🎶 Music Libraries Found:")
        for section in music_sections:
            print(f"\n📁 Library: {section.title}")
            for location in section.locations:
                print(f"   - Path: {location}")
    except Exception as e:
        print(f"❌ Error connecting to Plex server: {e}")

if __name__ == "__main__":
    get_music_library_paths()