### Functions to transform raw data into workable form ###

### creating a decade column
def to_decade_int(year):
    if year < 1930:
        return 0
    elif year < 1940:
        return 1
    elif year < 1950:
        return 2
    if year < 1960:
        return 3
    elif year < 1970:
        return 4
    elif year < 1980:
        return 5
    elif year < 1990:
        return 6
    elif year < 2000:
        return 7
    else:
        return 8


def to_decade_str(year):
    if year < 1930:
        return '1920s'
    elif year < 1940:
        return '1930s'
    elif year < 1950:
        return '1940s'
    if year < 1960:
        return '1950s'
    elif year < 1970:
        return '1960s'
    elif year < 1980:
        return '1970s'
    elif year < 1990:
        return '1980s'
    elif year < 2000:
        return '1990s'
    else:
        return ' new millenium'


### To help one see the track/song keys.  
def to_keyName(key):
    keys = dict(zip(range(12), ['C','C#','D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']))
    if key in keys: 
        return keys[key]
    else:
        return '-1'
### Display major or minor
def to_quality(mode):
    if mode == 1:
        return ' Major'
    else:
        return ' minor'
### change time signature to account for 3/4, 4/4 and other. 
def aggregate_time_sig(time_sig):
	if time_sig == 4:
		return 0
	elif time_sig == 3:
		return 1
	else:
		return 2


### Exploring if a genre is in an artists' tags
def genre(x):
    if x in terms_dict_spcf:
        return terms_dict_spcf[x]
    else:
        return 0


### remove outlier tempos
def tempo_correction(tempo):
    if tempo < 25:
        return 120
    else: return tempo


### remove outlier 


if __name__ == '__main__':
	
	df['decade'] = map(to_decade, df['year'])
