import requests 
import json
import webbrowser as w

client_id = "client_id"
client_secret = "client_secret"
encoded_id = "encoded_id"
redirect = "https://example.com/"
playlist_id = "playlist_id"

auth_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
liked_url = "https://api.spotify.com/v1/me/tracks"
playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

class spotify_client:
    def get_code(self):
        payload = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect,
            "scope": "user-library-read playlist-modify-public"
        }

        r = requests.get(auth_url, params = payload)
        return r.url
    
    def get_token(self, code):
        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect
        }
        r = requests.post(token_url, auth = (client_id, client_secret), data = payload)

        try:
            token = r.json()["access_token"]
            return token
        except KeyError:
            print("Invalid Code")

    def get_liked(self, token):
        header = {
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "limit": 50,
            "offset": 0
        }
        song_uris = []

        for i in range(0, 10):
            r = requests.get(liked_url, params = payload, headers = header)
            package = r.json()
            payload["offset"] += 50
            for item in package["items"]:
                song_uris.append(item["track"]["uri"])

        return song_uris
    
    def get_playlist_songs(self, token, id):
        header = {
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "market": "from_token",
            "offset": 0
        }
        song_uris = []

        for i in range(0, 5):
            r = requests.get(playlist_url, params = payload, headers = header)
            payload["offset"] += 100
            package = r.json()

            for item in package["items"]:
                if item["track"]["uri"] not in song_uris:
                    song_uris.append(item["track"]["uri"])
                    print(item["track"]["name"])        
        return song_uris

    def add_songs(self, token, songs, playlist):
        uris = []

        for song in songs:
            if song not in playlist:
                uris.append(song)

        header = {
            "Content_Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        for i in range(0, len(uris), 100):
            end = min(len(uris) - i, i + 100)
            selection = uris[i:end]
            params = json.dumps(selection)
            r = requests.post(playlist_url, data = params, headers = header)
            print(r.text)

def main():
    client = spotify_client()
    auth_site = client.get_code()
    w.open_new(auth_site)
    code = input("Enter code: ")
    
    token = client.get_token(code)
    songs = client.get_liked(token)
    playlist = client.get_playlist_songs(token, playlist_id)
    client.add_songs(token, songs, playlist)

main()