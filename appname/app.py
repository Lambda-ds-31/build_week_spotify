import spotipy
from flask import Flask
from flask import render_template
from flask import request
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pandas as pd
from .recommeder import find_knn


def create_app():

    load_dotenv()

    app = Flask(__name__)

    api_key = os.getenv("api_key")
    secret_key = os.getenv("secret_key")

    manager = SpotifyClientCredentials(client_id=api_key, client_secret=secret_key)
    sp = spotipy.Spotify(client_credentials_manager=manager)

    def describe_track(id):
        """ takes a track id and returns dictionary with
        descriptive information """

        attributes = sp.track(id)

        name = attributes['name']
        artist = attributes['artists']['name']
        album = attributes['album']['name']
        album_url = attributes['album']['external_urls']['spotify']
        track_url = attributesttributes['external_urls']['spotify']

        description = {
            'name': name,
            'artist': artist,
            'album': album,
            'album_url': album_url,
            'track_url': track_url
            }

    def track_features(id):
        """ takes a track id and returns a dictionary with its features """
        dict = sp.audio_features(id)[0]

        drops = ['key', 'mode', 'type', 'id',
        'uri', 'track_href', 'analysis_url',
        'time_signature']

        for drop in drops:
            del dict[drop]

    @app.route('/', methods=['GET', "POST"])
    def root():
        """ Base page """

         name = request.form.get('name')# name can be multiple terms

         # gets the id of the top search result
         id = sp.search(name, type='track', limit=1)['tracks']['items'][0]['id']

         recs = find_knn(id) # pass the id to Xianshi's function

         named_recs = []
         for rec in recs:
             named_recs.append(describe_track(rec))

        tracks_atts = track_features(id)

         return render_template('home.html',
            title = 'Home',
            recs = named_recs,
            track_atts = tracks_atts)
