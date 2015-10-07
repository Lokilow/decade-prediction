from wtforms import Form, FloatField, validators, IntegerField, SelectField
import random

class InputForm(Form):
    acousticness= FloatField(
        label='acousticness', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    danceability = FloatField(
        label='danceability', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    duration = SelectField(
        label='duration', default=250.,
        choices=[(random.randrange(60., 200., 3.), 'short - under 3 minutes'), 
        (random.randrange(200., 330., 3.), 'medium - 3 to 5 minutes'), 
            (random.randrange(330., 550., 3.) , 'long - over 5 minutes')],
        coerce=float)
    energy = FloatField(
        label='energy', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    instrumentalness = FloatField(
        label='instrumentalness', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    liveness = FloatField(
        label='liveness', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    loudness = FloatField(
        label='loudness', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(-50, 3)])
    mode = SelectField(label='mode', default=0, 
        choices=[(0,'minor'), (1, 'Major')], coerce=float)
    speechiness = FloatField(
        label='speechines', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])
    tempo = IntegerField(
        label='tempo', default=120,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 250)])
    time_signature = SelectField(
        label='time_signature', default=4,
        choices=[(4, '4/4'), (3, '3/4'), (5 , 'other')],
        coerce=float)
    valence = FloatField(
        label='valence', default=0.5,
        validators=[validators.InputRequired(),
        validators.NumberRange(0, 1)])

