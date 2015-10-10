import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import pickle
import sys

###TRACKS
def track_plot(FEATURE):
    t_years = info_dict['track_maxes'].index
    x_max = info_dict['track_maxes'][FEATURE]
    x_min = info_dict['track_mins'][FEATURE]
    x_mean = info_dict['track_means'][FEATURE]
    x_std_pos = info_dict['track_means'][FEATURE] + 2*info_dict['track_sds'][FEATURE]
    x_std_neg = info_dict['track_means'][FEATURE] - 2*info_dict['track_sds'][FEATURE]

    trace_max = Scatter(
        x=t_years,
        y=x_max,
        mode='markers',
        name="max Track " + FEATURE,
        marker=Marker(size='4',
    ))

    trace_min = Scatter(
        x=t_years,
        y=x_min,
        mode='markers',
        name="min Track " + FEATURE,
        marker=Marker(size='4',
    ))

    trace_mean = Scatter(
        x=t_years,
        y=x_mean,
        mode='lines',
        name="mean Track " + FEATURE,
        marker=Marker(size='8',
    ))
    trace_std_pos = Scatter(
        x=t_years,
        y=x_std_pos,
        mode='lines',
        name="+2 std. dev Track " + FEATURE,
        marker=Marker(size='4',
    ))
    trace_std_neg = Scatter(
        x=t_years,
        y=x_std_neg,
        mode='lines',
        name="-2 std. dev Track " + FEATURE,
        marker=Marker(size='4',
    ))




    # Package the trace dictionary into a data object
    data = Data([trace_max, trace_min, trace_mean, trace_std_pos, trace_std_neg])
    layout=Layout(
    title="Track \'"+ FEATURE[0].upper() + FEATURE[1:] + "\' vs. Year"
    )
    fig = Figure(data=data, layout=layout)
    return py.plot(fig)

###songS
def song_plot(FEATURE):
    t_years = song_maxes.index
    x_max = song_maxes["song_" + FEATURE]
    x_min = song_mins["song_" + FEATURE]
    x_mean = song_means["song_" + FEATURE]
    x_std_pos = song_means["song_" + FEATURE] + song_stds["song_" + FEATURE]
    x_std_neg = song_means["song_" + FEATURE] - song_stds["song_" + FEATURE]

    trace_max = Scatter(
        x=t_years,
        y=x_max,
        mode='markers',
        name="max song " + FEATURE,
        marker=Marker(size='4',
    ))

    trace_min = Scatter(
        x=t_years,
        y=x_min,
        mode='markers',
        name="min song " + FEATURE,
        marker=Marker(size='4',
    ))

    trace_mean = Scatter(
        x=t_years,
        y=x_mean,
        mode='lines',
        name="mean song " + FEATURE,
        marker=Marker(size='8',
    ))
    trace_std_pos = Scatter(
        x=t_years,
        y=x_std_pos,
        mode='lines',
        name="+1 std. dev song " + FEATURE,
        marker=Marker(size='4',
    ))
    trace_std_neg = Scatter(
        x=t_years,
        y=x_std_neg,
        mode='lines',
        name="-1 std. dev song " + FEATURE,
        marker=Marker(size='4',
    ))




    # Package the trace dictionary into a data object
    data = Data([trace_max, trace_min, trace_mean, trace_std_pos, trace_std_neg])
    layout=Layout(
    title="Song \'"+ FEATURE[0].upper() + FEATURE[1:] + "\' vs. Year"
    )
    fig = Figure(data=data, layout=layout)
    return py.plot(fig)


###Histograms
### getting the histogram features

# t11 = _eighties.drop(['decade', 'time_sig','mode', 'acousticness', 'energy', 'valence', \
#                  'danceability', 'liveness', 'm_ac', 'm_en', 'm_v', 'm_inst', 'm_dnc', 'm_lv'], axis=1).mean()
# t12 = _eighties.drop(['decade', 'time_sig','mode', 'acousticness', 'energy', 'valence', \
#                  'danceability', 'liveness', 'm_ac', 'm_en', 'm_v', 'm_inst', 'm_dnc', 'm_lv'], axis=1).var()
# t21 = _new_millenium.drop(['decade', 'time_sig','mode', 'acousticness', 'energy', 'valence', \
#                  'danceability', 'liveness', 'm_ac', 'm_en', 'm_v', 'm_inst', 'm_dnc', 'm_lv'], axis=1).mean()
# t22 = _new_millenium.drop(['decade', 'time_sig','mode', 'acousticness', 'energy', 'valence', \
#                  'danceability', 'liveness', 'm_ac', 'm_en', 'm_v', 'm_inst', 'm_dnc', 'm_lv'], axis=1).var()

# ### Feature Histogram

# trace0 = Bar(
#     x=list(t11.index),
#     y=t11.values,
#     name='sixties',
#     marker=Marker(
#         color='rgb(49,130,189)',
#         opacity=0.7,
#     ),
# )
# trace1 = Bar(
#     x=list(t21.index),
#     y=t21.values,
#     name='eighties',
#     marker=Marker(
#         color='rgb(204,204,204)',
#         opacity=0.5,
#     ),
# )
# data = Data([trace0, trace1])
# layout = Layout(
#     xaxis=XAxis(
#         # set x-axis' labels direction at 45 degree angle
#         tickangle=-45,
#     ),
#     barmode='group',
# )
# fig = Figure(data=data, layout=layout)
# py.iplot(fig, filename='angled-text-bar')


# trace0 = Bar(
#     x=list(t12.index),
#     y=t11.values,
#     name='sixties_sd',
#     marker=Marker(
#         color='rgb(49,130,189)',
#         opacity=0.7,
#     ),
# )
# trace1 = Bar(
#     x=list(t22.index),
#     y=t21.values,
#     name='eighties_sd',
#     marker=Marker(
#         color='rgb(204,204,204)',
#         opacity=0.5,
#     ),
# )
# data = Data([trace0, trace1])
# layout = Layout(
#     xaxis=XAxis(
#         # set x-axis' labels direction at 45 degree angle
#         tickangle=-45,
#     ),
#     barmode='group',
# )
# fig = Figure(data=data, layout=layout)
# py.iplot(fig, filename='angled-text-bar')

if __name__ == '__main__':
    info_dict = pickle.load(open('../valence_space_data/data/graph_info_byyear_dict.p', 'rb'))
    for feature in sys.argv[1:]:
        track_plot(feature)



