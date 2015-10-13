import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import pickle
import sys


tracks = pickle.load(open(
    '../valence_space_data/data/clean_tracks.p', 'rb'))

info_dict = pickle.load(open(
    '../valence_space_data/data/graph_info.p', 'rb'))


# For tracks
def track_plot(FEATURE):
    t_years = info_dict['track_means'].index
    x_max = info_dict['track_upper_q'][FEATURE]
    x_min = info_dict['track_lower_q'][FEATURE]
    x_mean = info_dict['track_means'][FEATURE]
    # x_std_pos = info_dict['track_means'][FEATURE] + \
    #     2*info_dict['track_sds'][FEATURE]
    # x_std_neg = info_dict['track_means'][FEATURE] - \
    #     2*info_dict['track_sds'][FEATURE]

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
        marker=Marker(size='8',))
    # trace_std_pos = Scatter(
    #     x=t_years,
    #     y=x_std_pos,
    #     mode='lines',
    #     name="+2 std. dev Track " + FEATURE,
    #     marker=Marker(size='4',))
    # trace_std_neg = Scatter(
    #     x=t_years,
    #     y=x_std_neg,
    #     mode='lines',
    #     name="-2 std. dev Track " + FEATURE,
    #     marker=Marker(size='4',))

    # Package the trace dictionary into a data object
    data = Data([trace_mean, trace_max, trace_min])
    layout = Layout(
        title="Track \'" + FEATURE[0].upper() + FEATURE[1:] + "\' vs. Year")
    fig = Figure(data=data, layout=layout)
    return py.plot(fig)


# For songs
def song_plot(FEATURE):
    t_years = song_maxes.index
    x_max = song_maxes["song_" + FEATURE]
    x_min = song_mins["song_" + FEATURE]
    x_mean = song_means["song_" + FEATURE]
    x_std_pos = song_means["song_" + FEATURE] + song_stds["song_" + FEATURE]
    x_std_neg = song_means["song_" + FEATURE] - song_stds["song_" + FEATURE]

    # trace_max = Scatter(
    #     x=t_years,
    #     y=x_max,
    #     mode='markers',
    #     name="max song " + FEATURE,
    #     marker=Marker(size='4',
    # ))

    # trace_min = Scatter(
    #     x=t_years,
    #     y=x_min,
    #     mode='markers',
    #     name="min song " + FEATURE,
    #     marker=Marker(size='4',
    # ))

    trace_mean = Scatter(
        x=t_years,
        y=x_mean,
        mode='lines',
        name="mean song " + FEATURE,
        marker=Marker(size='8',))
    trace_std_pos = Scatter(
        x=t_years,
        y=x_std_pos,
        mode='lines',
        name="+1 std. dev song " + FEATURE,
        marker=Marker(size='4',))
    trace_std_neg = Scatter(
        x=t_years,
        y=x_std_neg,
        mode='lines',
        name="-1 std. dev song " + FEATURE,
        marker=Marker(size='4',))

    # Package the trace dictionary into a data object
    data = Data([trace_mean, trace_std_pos, trace_std_neg])
    layout = Layout(
        title="Song \'" + FEATURE[0].upper() + FEATURE[1:] + "\' vs. Year"
    )
    fig = Figure(data=data, layout=layout)
    return py.plot(fig)


def histplot(feature):

    # Add histogram data and feature labels
    x = tracks[feature]
    data = Data([
            Histogram(
                x=x
            )
        ])
    return py.iplot(data)


if __name__ == '__main__':
    for feature in sys.argv[1:]:
        track_plot(feature)
