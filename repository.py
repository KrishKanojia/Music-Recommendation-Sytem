import requests
import base64
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID_KEY = os.getenv("CLIENT_ID_KEY")
CLIENT_SECRET_KEY = os.getenv("CLIENT_SECRET_KEY")

def gen_access_token():
    # Base64 encode
    client_credentials = f"{CLIENT_ID_KEY}:{CLIENT_SECRET_KEY}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    # Request Access Token
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}' 
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
        return access_token
    else:
        print("Error obtaining access token.")
        exit()
    

def get_trending_playlist_data(playlist_id = '37i9dQZF1DX76Wlfdnj7AP'):
    access_token = gen_access_token()

    # Set up Spotify using Access Token
    sp = spotipy.Spotify(auth=access_token)

    # Get track from the playlist
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id, name, artists, album(id, name)))')

    # Extract Relevant Information
    music_data = []
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_id = track['id']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
    
        # Get audio features from track
        audio_features = sp.audio_features(track_id)[0] if track_id != 'Not available' else None

        # Get release date of the album
        try:
            album_info = sp.album(album_id) if album_id != 'Not available' else None
            release_date = album_info['release_date'] if album_info else None

        except:
            release_date = None

        try:
            track_info = sp.track(track_id) if track_id != 'Not available' else None
            popularity = track_info['popularity'] if track_info else None
        except:
            popularity = None
        
        # Add additional Info to track data
        track_data = {
            'Track Name': track_name,
            'Album Name': album_name,
            'Artists': artists,
            'Track ID': track_id,
            "Album ID": album_id,
            'Popularity': popularity,
            'Release Date': release_date,
            'Duration (ms)': audio_features['duration_ms'] if audio_features else None,
            'Explicit': track_info.get('explicit', None),
            'External URLs': track_info.get('external_urls', {}).get('spotify', None),
            'Danceability': audio_features['danceability'] if audio_features else None,
            'Energy': audio_features['energy'] if audio_features else None,
            'Key': audio_features['key'] if audio_features else None,
            'Loudness' : audio_features['loudness'] if audio_features else None,
            'Mode' : audio_features['mode'] if audio_features else None,
            'Speechiness' : audio_features['speechiness'] if audio_features else None,
            'Acousticness' : audio_features['acousticness'] if audio_features else None,
            'Instrumentalness' : audio_features['instrumentalness'] if audio_features else None,
            'Liveness' : audio_features['liveness'] if audio_features else None,
            'Valence' : audio_features['valence'] if audio_features else None,
            'Tempo' : audio_features['tempo'] if audio_features else None,
        }
        music_data.append(track_data)

    # Create Pandas Dataframe from music_data List Dictionaries
    df = pd.DataFrame(music_data)
    
    return df   
        
# if __name__ == "__main__":
#     playlist_id = '37i9dQZF1DX76Wlfdnj7AP'
#     # access_token = gen_access_token()
#     MUSIC_DATA = get_trending_playlist_data(playlist_id)
#     print(MUSIC_DATA)   
