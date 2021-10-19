import numpy as np
from data_prep import data
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv


client_id = getenv('CLIENT_ID')
client_id_secret = getenv('CLIENT_ID_SECRET')
manager = SpotifyClientCredentials(client_id = client_id, client_secret= client_id_secret)
sp = spotipy.Spotify(client_credentials_manager=manager)

def find_knn(track_id, df, k=6):
    """
    Takes in the user input song's track_id, and the prep-ed dataframe.
    Outputs a list of k-1 nearest neighbors based on audio features
    """
    features = sp.audio_features(track_id)[0] 
    df = data()
    user_track = np.array(
        [
            features['acousticness'], 
            features['danceability'], 
            features['duration_ms'], 
            features['energy'], 
            features['instrumentalness'], 
            features['liveness'], 
            features['loudness'], 
            features['speechiness'], 
            features['tempo'], 
            features['valence']
        ]
    )
    df['distances'] = np.linalg.norm(df - user_track, axis=1)
    nn_ids = df.sort_values(by='distances').index.to_list()[:k]
    
    if nn_ids[0] == track_id:
        nn_ids = nn_ids[1:]
    else:
        nn_ids = nn_ids[:-1]

    return nn_ids