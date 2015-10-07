from flask import Flask, render_template, request
import random
from classify import predict_decade
import sys
from feature_inputs import InputForm


try:
    template_name = sys.argv[1]
except IndexError:
    template_name = 'front'


app = Flask(__name__)

if template_name == 'view_flask_bootstrap':
    from flask_bootstrap import Bootstrap
    Bootstrap(app)



# View
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = predict_decade(form.acousticness.data, form.danceability.data,
            form.duration.data, form.energy.data, form.instrumentalness.data, form.liveness.data,
            form.loudness.data, form.mode.data, form.speechiness.data, form.tempo.data,
            form.time_signature.data, form.valence.data)
    else:
        result = None

    return render_template(template_name + '.html', form=form, result=result)

@app.route('/playlist')
def playlist():
    return render_template('front.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

# @app.route('/playlist')
# def playlist():
#     valence = request.form["valence"]
#     danceability = request.form["danceability"]
#     liveness = request.form["liveness"]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
