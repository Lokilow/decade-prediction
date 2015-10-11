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
from feature_engineering import to_grouped_decades


tracks = pickle.load(open('../../valence_space_data/data/tracks.p', 'rb'))
tracks.drop(['song_id', 'track_id'], axis=1, inplace=True)

## clean up labels
tracks.columns = ['mode', 'acousticness', 'artist', 'energy', 'valence', 'instrumentalness', 'year', 'track_name', \
                 'key', 'duration', 'loudness', 'time_signature', 'tempo', 'speechiness', 'danceability', 'liveness']

tracks['decade'] = map(to_grouped_decades, tracks['year']) 
_tracks = tracks.drop(['artist', 'track_name'], axis=1)

# change order of columns
organized = _tracks[['key', 'mode', 'time_signature', 'tempo', 'loudness', 'duration', 'acousticness', 'danceability', 'energy', \
                          'instrumentalness', 'liveness', 'speechiness', 'valence', 'year', 'decade']]

# create dummy variables
dummied = pd.concat([organized, pd.get_dummies(_tracks['key'])], axis=1)
dummied = pd.concat([dummied, pd.get_dummies(dummied['time_signature'])], axis=1)

track_list = zip(tracks['artist'], tracks['track_name'])
track_id_list = list(tracks.index)
track_dict = dict(zip(track_id_list, track_list))


if __name__ == '__main__':

	f = open('../../valence_space_data/data/clean_tracks.p', 'wb')
    pickle.dump(organized, f)
    f.close()
    
    f = open('../../valence_space_data/data/track_dict.p', 'wb')
    pickle.dump(track_dict, f)
    f.close()
    
    f = open('../../valence_space_data/data/dummied_df.p', 'wb')
    pickle.dump(dummied_df, f)
    f.close()
