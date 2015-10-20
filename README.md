An exploration of the million song dataset and classifying music by decade using Echo Nest audio features.

Motivation

Every decade has its own unique musical sound.  When I listen to new music, I try to place that music in a past sound.  Since art always builds on itself, this is a good way to explore an artist's influences, and also to see what specific sounds the artist may have blended together.  I wanted to see if I could come up with a machine learning algortithm that would do just this.

Getting Started

I turned to the 2011 Million Song Dataset for my data.  After taking a look at what was in the database, and taking a look at the current state of The Echo Nest, I decided it would be best to simply take a list of ids from the set and re-query the Echo Nest API for updated information.  The Echo Nest has an audio analysis algorithm that takes in the waveforms of a song, and grades the song in thirteen different categories.  Some of the features are somewhat abstruse and subjective, such as energy and danceability (A George Harrison song scored higher on danceability than any Michael Jackson song!!?), and others were more concrete, such as tempo and key.  After going through all of the tracks, I was left with around 270,000 that had a year tag and all of the Echo Nest features.  

Data

I did not include the data in this repo because it was a bit large for GitHub

Analysis
I used Plotly to generate graphs of the distributions of my data and the averages over time.  I noticed many of the trends seem to correspond to musical technology of the time.  After exploring a number of classifiers and a linear regression to predict decade, a random forest model proved the most accurate, achieving a 5 fold cross-validation accuracy of 53 percent (compared to 6.7 percent by chance).

