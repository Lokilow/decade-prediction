import pandas as pd
import numpy as np
import pickle
from collections import defaultdict
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':


    tracks = pickle.load(open('DataSetCreation/data/tracks.p', 'rb'))
    tracks.drop(['song_id', 'track_id'], axis=1, inplace=True)


    tracks.columns = ['mode', 'acousticness', 'artist', 'energy', 'valence', 'instrumentalness', 'year', 'track_name', \
                     'key', 'duration', 'loudness', 'time_signature', 'tempo', 'speechiness', 'danceability', 'liveness']

    
    _tracks = tracks.drop(['artist', 'track_name','key'], axis=1)
    ### Adding decade for classification modelling
    # _tracks['decade'] = map(to_decade, tracks['year'])

    _tracks['total_beats'] = (_tracks['tempo'] / 60.) * _tracks['duration']
    _tracks['total_bars'] = _tracks['total_beats'] / (map(lambda x: float(x), _tracks['time_signature'] + 1))

    duration_scaler = StandardScaler()
    _tracks['duration'] = duration_scaler.fit_transform(_tracks['duration'])

    loudness_scaler = StandardScaler()
    _tracks['loudness'] = loudness_scaler.fit_transform(_tracks['loudness'])

    tempo_scaler = StandardScaler()
    _tracks['tempo'] = tempo_scaler.fit_transform(_tracks['tempo'])

    total_beats_scaler = StandardScaler()
    _tracks['total_beats'] = total_beats_scaler.fit_transform(_tracks['total_beats'])

    total_bars_scaler = StandardScaler()
    _tracks['total_bars'] = total_bars_scaler.fit_transform(_tracks['total_bars'])


    ##interaction terms
    _tracks['metalness'] = _tracks['energy'] * _tracks['instrumentalness']
    # _tracks['metalness'] = scaler.fit_transform(_tracks['metalness'])

    _tracks['metalness2'] = _tracks['energy'] * _tracks['danceability']
    # _tracks['metalness2'] = scaler.fit_transform(_tracks['metalness2'])

    _tracks['metalness3'] = _tracks['energy'] / (_tracks['danceability'] + 0.01)
    # _tracks['metalness3'] = scaler.fit_transform(_tracks['metalness3'])

    _tracks['duration_loudness'] = _tracks['duration'] * _tracks['loudness']
    # _tracks['duration_loudness'] = scaler.fit_transform(_tracks['duration_loudness'])

    _tracks['acousticness_energy'] = _tracks['acousticness'] * _tracks['energy']
    # _tracks['acousticness_energy'] = scaler.fit_transform(_tracks['acousticness_energy'])

    _tracks['acousticness_liveness'] = _tracks['acousticness'] * _tracks['liveness']
    # _tracks['acousticness_liveness'] = scaler.fit_transform(_tracks['acousticness_liveness'])

    _tracks['mood'] = _tracks['energy'] * _tracks['valence']
    # _tracks['mood'] = scaler.fit_transform(_tracks['mood'])

    _tracks['valence_tempo'] = _tracks['valence'] / (_tracks['tempo'] + 0.001)
    # _tracks['valence_tempo'] = scaler.fit_transform(_tracks['valence_tempo'])

    _tracks['hip_hop1'] = _tracks['speechiness'] * _tracks['loudness']
    # _tracks['hip_hoph1'] = scaler.fit_transform(_tracks['hip_hop1'])

    _tracks['hip_hop2'] = _tracks['speechiness'] * _tracks['danceability']
    # _tracks['hip_hop2'] = scaler.fit_transform(_tracks['hip_hop2'])

    _tracks['hip_hop3'] = _tracks['speechiness'] * _tracks['valence']
    # _tracks['hip_hop3'] = scaler.fit_transform(_tracks['hip_hop3'])

    _tracks['hip_hop4'] = _tracks['speechiness'] * _tracks['tempo']
    # _tracks['hip_hop4'] = scaler.fit_transform(_tracks['hip_hop4'])






    #Mode * 
    _tracks['mode_accousticness'] = _tracks['mode'] * _tracks['acousticness']
    _tracks['mode_energy'] = _tracks['mode'] * _tracks['energy']
    _tracks['mode_valence'] = _tracks['mode'] * _tracks['valence']
    _tracks['mode_instrumentalness'] = _tracks['mode'] * _tracks['instrumentalness']
    # _tracks['mode_duration'] = _tracks['mode'] * _tracks['duration']
    _tracks['mode_loudness'] = _tracks['mode'] * _tracks['loudness']
    _tracks['mode_tempo'] = _tracks['mode'] * _tracks['tempo']
    _tracks['mode_speechiness'] = _tracks['mode'] * _tracks['speechiness']
    _tracks['mode_danceability'] = _tracks['mode'] * _tracks['danceability']
    _tracks['mode_liveness'] = _tracks['mode'] * _tracks['liveness']
    _tracks['mode_metalness'] = _tracks['mode'] * _tracks['metalness']
    _tracks['mode_metalness2'] = _tracks['mode'] * _tracks['metalness2']
    # _tracks['mode_duration_loudness'] = _tracks['mode'] * _tracks['duration_loudness']
    _tracks['mode_acousticness_energy'] = _tracks['mode'] * _tracks['acousticness_energy']
    _tracks['mode_mood'] = _tracks['mode'] * _tracks['mood']
    # _tracks['mode_valence_tempo'] = _tracks['mode'] * _tracks['valence_tempo']

    print _tracks.columns
    ### modelling
    model = RandomForestRegressor()
    X_train, X_test, y_train, y_test = \
    train_test_split(_tracks.drop(['year', 'total_beats'], axis=1), _tracks['year'])

    model.fit(X_train, y_train)

    pickle_list = [duration_scaler, loudness_scaler, tempo_scaler, total_beats_scaler, total_bars_scaler, \
                  model]
    pickle_names = ['duration_scaler', 'loudness_scaler', 'tempo_scaler', 'total_beats_scaler', 'total_bars_scaler', \
                  'model']
    model_dict = dict(zip(pickle_names, pickle_list))

    f = open('model/model_dict.p', 'wb')
    pickle.dump(model_dict, f)
    f.close()

    pred = model.predict(X_test)
    print sm.f1_score(pred.round(), y_test)
    print sm.f1_score(map(to_decade, y_test), map(to_decade, pred))
    print sm.accuracy_score(map(to_decade, y_test), map(to_decade, pred))
    print model.score(X_test, y_test)
    print sm.mean_squared_error(pred.round(), y_test)
    print sm.mean_absolute_error(pred.round(), y_test)




