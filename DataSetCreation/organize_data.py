import pandas as pd
import numpy as np
import pickle
from collections import defaultdict
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import cross_val_score


### create decade target
def to_decade(year):
    decade = (year - 1950) // 10
    if decade < 0:
        return 0
    elif decade > 5:
        return 5
    else:
        return decade

tracks = pickle.load(open('../../valence_space_data/data/tracks.p', 'rb'))
print tracks.columns
tracks.drop(['song_id', 'track_id'], axis=1, inplace=True)


## clean up 
tracks.columns = ['mode', 'acousticness', 'artist', 'energy', 'valence', 'instrumentalness', 'year', 'track_name', \
                 'key', 'duration', 'loudness', 'time_signature', 'tempo', 'speechiness', 'danceability', 'liveness']

tracks['decade'] = map(to_decade, tracks['year']) 
_tracks = tracks.drop(['artist', 'track_name'], axis=1)

organized = _tracks[['key', 'mode', 'time_signature', 'tempo', 'loudness', 'duration', 'acousticness', 'danceability', 'energy', \
                          'instrumentalness', 'liveness', 'speechiness', 'valence', 'year', 'decade']]


track_list = zip(tracks['artist'], tracks['track_name'])
track_id_list = list(tracks.index)
track_dict = dict(zip(track_id_list, track_list))


f = open('../../valence_space_data/data/cleanTracks.p', 'wb')
pickle.dump(organized, f)
f.close()


f = open('../../valence_space_data/data/track_dict.p', 'wb')
pickle.dump(track_dict, f)
f.close()