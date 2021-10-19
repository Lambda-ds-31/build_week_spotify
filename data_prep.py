import pandas as pd

test_id = '2tJulUYLDKOg9XrtVkMgcJ'


def data():
    
    df = pd.read_csv('SpotifyFeatures.csv')
    df = df.drop(
        columns=[
            'genre',
            'artist_name',
            'track_name',
            'key',
            'mode',
            'time_signature',
            'popularity'
            ]
        )
    df = df.drop_duplicates(subset=['track_id'])
    df = df.set_index('track_id')
    
    return df