##### Creating the Data Frame #####

import pandas as pd
import numpy as np
import pickle
import sqlite3
from collections import defaultdict, Counter
import unicodedata

### Importing the pickled data dictionaries ###
_25 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_25.p', 'rb'))
_50 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_50.p', 'rb'))
_75 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_75.p', 'rb'))
_100 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_100.p', 'rb'))
_150 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_150.p', 'rb'))
_200 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_200.p', 'rb'))
_250 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_250.p', 'rb'))
_300 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_300.p', 'rb'))
_350 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_350.p', 'rb'))
_400 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_400.p', 'rb'))
_450 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_450.p', 'rb'))
_500 = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_500.p', 'rb'))
_end = pickle.load(open('../../valence_space_data/pickled_data/pickled_data_end.p', 'rb'))


### A list of the pickled data ###
pickles = [_25, _50, _75, _100, _150, _200, _250, _300, _350, _400, _end]
all_ = _25.copy()

### creating a dictionary of all data  ###
for data_slice in pickles[1:]:
	all_.update(data_slice)

### to a Data Frame ###
df = pd.DataFrame.from_dict(all_, orient='index')

### Splitting the data into song/track subsections
all_features = (_25.values()[0]).keys()   #the first track has a valid echonest song and track id.  Other data points
										  #may only have one of the two, such as the track id below

original_track_features = _25['TRIMKIC128F4271EA8'].keys()
original_song_features = [x for x in all_features if x not in original_track_features] + \
						 ['track_name', 'year', 'artist', 'song_id']


### Aggregation of artist terms.  Only data from valid song ids contains the artist musicbrainz id, which is where the tags 
### are coming from.

connection1 = sqlite3.connect('../../track_metadata.db')
df_track_metadata = pd.read_sql_query('select * from songs', connection1)

connection2 = sqlite3.connect('../../artist_term.db')
df_artist_mbtag = pd.read_sql_query('select * from artist_mbtag', connection2)
df_artist_term = pd.read_sql_query('select * from artist_term', connection2)
df_artist_artists = pd.read_sql_query('select * from artists', connection2)
df_mbtags = pd.read_sql_query('select * from mbtags', connection2)
df_terms = pd.read_sql_query('select * from terms', connection2)

###to aggregate all terms
def term_aggregation(terms_dict):
	for index, row in df_artist_mbtag.iterrows():
	    terms_dict[row['artist_id']] += [row['mbtag']]

	for index, row in df_artist_term.iterrows():
	    terms_dict[row['artist_id']] += [row['term']]
	return terms_dict



def from_unicode(u):					### translate from unicode
    return unicodedata.normalize('NFKD', u).encode('ascii','ignore')

def uniDict_to_strDict(terms_dict):
	for key, value in terms_dict.iteritems():        
		terms_dict[key] = map(from_unicode, terms_dict[key])
	return terms_dict







song_features = ['song_id', 'artist_id', 'artist', 'track_name', 'song_key', 'song_mode', 'song_time_signature', \
				'song_tempo', 'song_duration', 'song_loudness', 'song_energy', 'song_danceability', \
				'song_liveness', 'song_acousticness', 'song_instrumentalness', 'sopeechiness', \
                 'song_valence', 'latitude', 'longitude', 'year']



if __name__ == '__main__':

	songs_all = df[original_song_features].dropna()
	tracks_all = df[original_track_features].dropna()
	tracks = tracks_all.drop(['track_status', 'sng_id'], axis=1)

	songs_artists = dict(songs_all[['artist_id', 'artist']]) #artists in my song dataset


	terms_dict = defaultdict(list)
	terms_dict = term_aggregation(terms_dict=terms_dict)
	terms_dict = uniDict_to_strDict(terms_dict)

	songs_artists_terms = defaultdict(list)
	for artist_id, term in terms_dict.iteritems():
		if artist_id in songs_artists:
			songs_artists_terms[artist_id] = term
		else:
			pass

	songs = songs_all[song_features]

	f = open('../../valence_space_data/data/terms_dict.p', 'wb')
	pickle.dump(terms_dict, f)
	f.close()

	f = open('../../valence_space_data/data/songs_all.p', 'wb')
	pickle.dump(songs_all, f)
	f.close()

	f = open('../../valence_space_data/data/songs_artists.p', 'wb')   ### terms dictionary of artists in songs
	pickle.dump(songs_artists, f)
	f.close()

	f = open('../../valence_space_data/data/songs_artists_terms.p', 'wb')  
	pickle.dump(songs_artists_terms, f)
	f.close()

	f = open('../../valence_space_data/data/songs.p', 'wb')
	pickle.dump(songs, f)
	f.close()

	f = open('../../valence_space_data/data/tracks.p', 'wb')
	pickle.dump(tracks, f)
	f.close()






