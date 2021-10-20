import spotipy
from flask import Flask
from flask import render_template
from flask import request
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pandas as pd
from .predict import find_knn
import os
import json


def create_app():

    load_dotenv()

    app = Flask(__name__)

    api_key = os.getenv("CLIENT_ID")
    secret_key = os.getenv("CLIENT_ID_SECRET")

    pred_df = pd.read_csv('SpotifyFeatures.csv', index_col='track_id')
    pred_df.drop(columns= ['genre', 'key', 'mode', 'time_signature'], inplace = True)
    pred_df['duration_ms'] = pred_df['duration_ms']/pred_df['duration_ms'].max()

    manager = SpotifyClientCredentials(client_id=api_key, client_secret=secret_key)
    sp = spotipy.Spotify(client_credentials_manager=manager)

    def describe_track(id):
        """ takes a track id and returns dictionary with
        descriptive information """

        rs = sp.track(id)
        # print(json.dumps(rs, indent=4))

        importante = {
            'name': rs['name'],
            'artist': rs['album']['artists'][0]['name'],
            'album': rs['album']['name'],
            'imageurl': rs['album']['images'][2]['url'],
            'release': rs['album']['release_date'],
            'track_url': rs['external_urls']['spotify'],
            'album_url': rs['album']['external_urls']['spotify'],
            'id': rs['id']}

        # name = attributes['name']
        # artist = attributes['artists']['name']
        # album = attributes['album']['name']
        # album_url = attributes['album']['external_urls']['spotify']
        # track_url = attributesttributes['external_urls']['spotify']

        # description = {
        #     'name': name,
        #     'artist': artist,
        #     'album': album,
        #     'album_url': album_url,
        #     'track_url': track_url
        #     }

        return importante

    def track_features(id):
        """ takes a track id and returns a dictionary with its features """
        dicty = sp.audio_features(id)[0]

        drops = ['key', 'mode', 'type', 'id',
        'uri', 'track_href', 'analysis_url',
        'time_signature']

        for drop in drops:
            dicty.pop(drop)

        return dicty

    @app.route('/', methods=['GET', "POST"])
    def root():
        """ Base page """

        name = request.form.get('name')# name can be multiple terms
        error = None

        # gets the id of the top search result
        try:
            id = sp.search(name, type='track', limit=1)['tracks']['items'][0]['id']

            recs = find_knn(id, pred_df) # pass the id to Xianshi's function
            # print(recs)

            named_recs = []
            for rec in recs:
                named_recs.append(describe_track(rec))

            search_results = describe_track(id)
            tracks_atts = track_features(id)
            search = True
        except:
            search = None
            search_results = None
            named_recs = []
            tracks_atts = {}

            if name:
                error = True

        attributes = []
        for attr, value in tracks_atts.items():
            text = f'{attr}: {value}'
            attributes.append(text)


        return render_template('home.html',
            search = search,
            sres = search_results,
            recs = named_recs,
            track_atts = attributes,
            error = error
        )

    return app
