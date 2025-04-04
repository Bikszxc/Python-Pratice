import json
import re
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class PlaylistManager:
    def __init__(self, filename="main_playlist.json"):
        self.filename = filename
        self.playlist = self.load_playlist()

    def load_playlist(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                playlist = []
                for song in data:
                    playlist_obj = Song(song["title"], song["artist"], song["duration"])
                    playlist.append(playlist_obj)
                return playlist
        except (FileNotFoundError, json.JSONDecodeError):
            return []
                    
    def save_playlist(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([
                    {
                        "title": song.title,
                        "artist": song.artist,
                        "duration": song.duration
                    }
                    for song in self.playlist
                ], file, indent=4)
        except Exception as e:
            print(f"Failed to save! {e}")

    def add_song(self, song):
        self.playlist.append(song)
        self.save_playlist()

    def remove_song(self, song_title):
        for song in self.playlist:
            if song_title == song.title:
                self.playlist.remove(song)
            else:
                print("Song not found!")

        self.save_playlist()
    
    def get_total_duration(self):
        total_seconds = 0
        for song in self.playlist:
            match = re.match(r'^(0?[0-9]|[1-5][0-9]):([0-5][0-9])$', song.duration)
            minutes, seconds = int(match.group(1)), int(match.group(2))
            total_seconds += (minutes * 60) + seconds

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if hours == 0:
            return f"{minutes:02}:{seconds:02}"
        else:
            return f"{hours:02}:{minutes:02}:{seconds:02}"

    def view_playlist(self):
        spacing = max(len(song.title) for song in self.playlist) + 5
        print("-" * (45 + spacing))
        print(f"{"No.":<5}{"Title":<{spacing}}{"Artist":<25}{"Duration"}")
        print("-" * (45 + spacing))
        for i, song, in enumerate(self.playlist, start=1):
            print(f"{i:<5}{song.title:<{spacing}}{song.artist:<25}{song.duration}")
        print("-" * (45 + spacing))
        print(f"Playlist Runtime: {(self.get_total_duration())}")

    def search_song(self, search):
        spacing = max(len(song.title) for song in self.playlist) + 5
        found_songs = [song for song in self.playlist if song.title.lower() == search.lower()]

        if not found_songs:
            found_songs = [song for song in self.playlist if song.artist.lower() == search.lower()]

        if found_songs:
            print("-" * (45 + spacing))
            print(f"{"Title":<{spacing}}{"Artist":<25}{"Duration"}")
            print("-" * (45 + spacing))
            for song in found_songs:
                print(f"{song.title:<{spacing}}{song.artist:<25}{song.duration}")
        else:
            print("Nothing found!")

def main():
    pm = PlaylistManager()

    while True:

        print('-' * 10 + 'Playlist Manager' + '-' * 10) 
        print('1. View Playlist')
        print('2. Search Song')
        print('3. Add Song')
        print('4. Remove Song')
        print('5. Exit')

        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                pm.view_playlist()
            case 2:
                print('SEARCH')
                search = input('Enter a song or an artist name: ')
                pm.search_song(search)
            case 3:
                pass
            case 4:
                pass
            case 5:
                exit()
            case _:
                print("Choice does not exist.")



if __name__ == main():
    main()