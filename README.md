# Spotify Song Selector

Lambda School - DS UNIT 3 Build Week Project

This application predicts which songs are most similar to an user input song title. Using the Spotify API, various features of the song input are analyzed using a k-1 next nearest neighbor analysis of the audio features. 

The goal of this project is to provide users with the ability to discover new music according to their favorite songs through the analysis of various features of the songs. 

## Build Status

Currently in development.

## Interface

Follow this link to see it in action: 
[Spotify Song Selector](https://radiant-scrubland-11374.herokuapp.com/)

#### Landing Page

Users input a song title into the query.

<img width="734" alt="initiial screenshot" src="https://user-images.githubusercontent.com/86363828/138159433-9687f67a-3891-4fc0-b3eb-a57a505f74ed.png">


#### Results Page

Users song query result is displayed to the left of the page and five recommended songs, based on analysis of the query features, are presented as a list to the right. The links from the songs open spotify to play each song. 

<img width="878" alt="initial screenshot 2" src="https://user-images.githubusercontent.com/86363828/138159444-25c842fd-06ea-452f-9756-d44cedaa0f70.png">


## Usage

#### Built with
The languages used for this project include:
- [Python](https://www.python.org/) 
- HTML/CSS

The packages used include:
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/doc/stable/index.html)
- [Scikit Learn](https://scikit-learn.org/stable/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

#### Features

The application uses Flask to power the search query/input. From the user input, the song title is passed through Spotipy's search functionality and generates the track_id and audio features. These features are then passed through the predict.py file which uses a K-1 Nearest Neighbors model to predict the songs whose features most closely resemble the input track. The track id's of the recommended songs are brought back through the front end and presented to the User as a list of songs with links to open the songs in Spotify. 

#### API Reference
[Spotify](https://developer.spotify.com/documentation/web-api/)\
Authentication and client credentials are required to access this application. An .env file is with "CLIENT_ID" and "CLIENT_SECRET" variables is required for use. 

## Contribute

TBD

## Team
Kevin Lynner (app.py, data_prep.py, flask and python master)\
Xianshi Wei (predict.py, modeling guru)\
Robert Davis (html/css, deployment hero)\
Bianca Klucik (along for the ride and writing things down, tbd visualizations)\
Alexis A Hombre \

## License

The MIT License (MIT)

Copyright (c) 2021 DS31 Spotify Group

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

