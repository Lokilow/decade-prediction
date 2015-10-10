import pyen
import spotipy
import sys
import urllib2
import json
from collections import defaultdict
import pickle
import time

track_list = pickle.load(open('tracknamelist.p', 'rr'))
tracklist = list(track_list.iteritems())
tracklist = map(lambda x: (x[0], x[1][0].replace(' ', '%'), x[1][1].replace(' ', '%')), tracklist)



if __name__ == '__main__':
	spotify_dict = defaultdict(str)
	counter = 0
	for i in xrange(len(tracklist)):
		if counter % 10 == 0:
			time.sleep(5)
		try:
			url = 'http://developer.echonest.com/api/v4/song/search?api_key=RJ7OB5YITVMP3EFS0&format=json&results=1&' + \
			'artist={!s}&title={!s}&bucket=id:spotify&bucket=tracks&limit=true'.format(tracklist[i][1], tracklist[i][2])
			data = json.load(urllib2.urlopen(url))
			spotify_dict[tracklist[i][0]] = data['response']['songs'][0]['tracks'][0]['foreign_id'].replace('spotify:track:', '')
			counter += 1
		except:
			print i, 'fail'

	f = open('all_ids.p', 'wb')
	pickle.dump(spotify_dict, f)
	f.close()