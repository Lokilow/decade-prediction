import pandas as pd
import numpy as np
import pickle
import numpy


def generate_playlist(df, acousticness, danceability, duration, energy, instrumentalness,
  liveness, loudness, mode, speechiness, tempo, time_signature, valence):
	playlist = df['spotify_id'].values[0:5]
	return str(",".join(playlist))
	# if total_count >= 25:
	# 	return np.random.choice(playlist, 25, replace=False)
	# elif total_count == 0:
	# 	return None
	# else:
	# 	return np.random.choice(playlist, total_count, replace=False)



# def playlist(*args):
# 	return 


if __name__ == '__main__':
	args = [sys.argv[1]] + map(float, sys.argv[2:])
	user_playlist = generate_playlist(args)
	print user_playlist

