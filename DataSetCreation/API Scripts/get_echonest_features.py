import pandas as pd
import numpy as np
from collections import defaultdict, Counter
from itertools import *
import sys
from pyechonest import song, track
from pyechonest import config
import pickle
import time
import sys


config.ECHO_NEST_API_KEY = "YOUR_ECHO_NEST_API_KEY"

# length of track_list: 515,576
track_list = pickle.load(
    open('../../../valence_space_data/data/trackList.p', 'rr'))


def get_track_features(start, stop):
    for num, track_info in enumerate(track_list[start:stop]):
        if num % 20 == 0:
            time.sleep(15)

        trk_id = track_info[0]
        year, song_id, artist, track_name = track_info[1]

        info_dict = dict()
        info_dict['year'] = year
        info_dict['artist'] = artist
        info_dict['track_name'] = track_name
        info_dict['track_id'] = trk_id
        info_dict['song_id'] = song_id
        tester = 0

        try:
            trk = track.track_from_id(trk_id)

            info_dict['track_acousticness'] = trk.acousticness
            info_dict['track_danceability'] = trk.danceability
            info_dict['track_duration'] = trk.duration
            info_dict['track_energy'] = trk.energy
            info_dict['track_instrumentalness'] = trk.instrumentalness
            info_dict['track_key'] = trk.key
            info_dict['track_liveness'] = trk.liveness
            info_dict['track_loudness'] = trk.loudness
            info_dict['track_mode'] = trk.mode
            info_dict['track_speechiness'] = trk.speechiness
            info_dict['track_tempo'] = trk.tempo
            info_dict['track_time_signature'] = trk.time_signature
            info_dict['track_valence'] = trk.valence

        except:
            print num, ' - track fail'
            tester += 1

        try:
            sawng = song.Song(song_id)
            location = sawng.get_artist_location()
            summary = sawng.get_audio_summary()

            # location
            info_dict['latitude'] = location['latitude']
            info_dict['longitude'] = location['longitude']
            info_dict['city'] = location['location']

            # audio summary
            info_dict['song_danceability'] = summary['danceability']
            info_dict['song_duration'] = summary['duration']
            info_dict['song_acousticness'] = summary['acousticness']
            info_dict['analysis_url'] = summary['analysis_url']
            info_dict['song_energy'] = summary['energy']
            info_dict['song_instrumentalness'] = summary['instrumentalness']
            info_dict['song_key'] = summary['key']
            info_dict['song_liveness'] = summary['liveness']
            info_dict['song_loudness'] = summary['loudness']
            info_dict['song_mode'] = summary['mode']
            info_dict['speechiness'] = summary['speechiness']
            info_dict['song_tempo'] = summary['tempo']
            info_dict['song_time_signature'] = summary['time_signature']
            info_dict['song_valence'] = summary['valence']

            # hotness, familiarity, and type
            info_dict['song_type'] = sawng.get_song_type()
            info_dict['artist_familiarity'] = sawng.get_artist_familiarity()
            info_dict['artist_hotttnesss'] = sawng.get_artist_hotttnesss()
            info_dict['song_currency'] = sawng.get_song_currency()
            info_dict['song_hotttnesss'] = sawng.get_song_hotttnesss()
            info_dict['artist_id'] = str(sawng.artist_id)
        except:
            print num, ' - song fail'
            tester += 1
        if tester < 2:
            trackDict[trk_id] = info_dict

        else:
            pass


if __name__ == '__main__':

    a, b = int(sys.argv[1]), int(sys.argv[2])
    trackDict = dict()

    get_track_features(a, b)
    f = open('../../../valence_space_data/pickled_data/pickled_data_{0!s}.p'
             .format(b), 'wb')
    pickle.dump(trackDict, f)
    f.close()
