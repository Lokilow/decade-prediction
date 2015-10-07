import pandas as pd
import numpy as np
import pickle
import os, time, glob
from collections import defaultdict
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import sys
sys.path.insert(0, '../DataSetCreation')
from feature_engineering import to_decade_str

model_dict = pickle.load(open('../../valence_space_data/model/model_dict.p', 'rb'))
##12 input features
def generate_features(acousticness, danceability, duration, energy, instrumentalness,
  liveness, loudness, mode, speechiness, tempo, time_signature, valence):
  
  total_beats = (tempo / 60.) * duration
  total_bars = total_beats / time_signature

  total_beats = model_dict['total_beats_scaler'].transform([total_beats])
  total_bars = model_dict['total_bars_scaler'].transform([total_bars])
  loudness = model_dict['loudness_scaler'].transform([loudness])
  duration = model_dict['duration_scaler'].transform([duration])
  tempo = model_dict['tempo_scaler'].transform([tempo])
  metalness  = energy * danceability
  metalness2 = energy * danceability
  metalness3 = energy / (danceability + 0.01)
  duration_loudness = duration * loudness
  acousticness_energy = acousticness * energy
  acousticness_liveness = acousticness * liveness
  mood = energy * valence
  valence_tempo = valence / (tempo + 0.001)
  hip_hop1 = speechiness * loudness
  hip_hop2 = speechiness * danceability
  hip_hop3 = speechiness * valence
  hip_hop4 = speechiness * tempo
  ## mode features
  mode_accousticness = mode * acousticness
  mode_energy = mode * energy
  mode_valence = mode * valence
  mode_instrumentalness = mode * instrumentalness
  mode_loudness = mode * loudness
  mode_tempo = mode * tempo
  mode_speechiness = mode * speechiness
  mode_danceability = mode * danceability
  mode_liveness = mode * liveness
  mode_metalness = mode * metalness
  mode_metalness2 = mode * metalness2
  mode_acousticness_energy = mode * acousticness_energy
  mode_mood = mode * mood

  return [mode, acousticness, energy, valence, instrumentalness,
       duration, loudness, time_signature, tempo, speechiness,
       danceability, liveness, total_bars,  metalness,
       metalness2,  metalness3, duration_loudness,
       acousticness_energy,  acousticness_liveness,  mood,
       valence_tempo,  hip_hop1,  hip_hop2,  hip_hop3,  hip_hop4,
       mode_accousticness,  mode_energy,  mode_valence,
       mode_instrumentalness,  mode_loudness,
       mode_tempo,  mode_speechiness,  mode_danceability,
       mode_liveness,  mode_metalness,  mode_metalness2,
       mode_acousticness_energy,  mode_mood]

def predict_decade(*args):
  model_args = generate_features(*args)
  prediction = model_dict['model'].predict(model_args)
  return to_decade_str(prediction)


if __name__ == '__main__':

  args = map(float, sys.argv[1:])
  print 'This song sounds like the ' + str(predict_decade(*args)) + '!'


