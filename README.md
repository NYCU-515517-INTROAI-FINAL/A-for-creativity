# A-for-creativity

## Environment

Python 3.11.3

## Package Dependencies


- [pandas 2.0.1](https://pypi.org/project/pandas/2.0.1/)
- [numpy 1.24.2](https://pypi.org/project/numpy/1.24.2/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [tabulate](https://pypi.org/project/tabulate/)
- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [scipy 1.10.1](https://docs.scipy.org/doc/scipy-1.10.1/getting_started.html)
- [plotly 5.14.1](https://plotly.com/python/getting-started/)
- [spotipy 2.23.0](https://github.com/spotipy-dev/spotipy)
- [fuzzywuzzy 0.18.0](https://pypi.org/project/fuzzywuzzy/)

## KNN

- Rely on the **_historical preference of users and other users' preference on a set of songs._**
- Discover the similarities on the user’s past behavior.
- Make predictions based on a similar preference with other users.
- A **non-parametric, unsupervised learning classifier.** 

## K-Means

- Assume that **_if a user has enjoyed certain songs in the past, they are likely to enjoy other songs that have similar features._**
- Produce recommendations based on its characteristics, such as its **genres, acousticness, danceability, tempo**, and etc.
- Doesn’t rely on data about other users' listening habits.Assume that if a user has enjoyed certain songs in the past, they are likely to enjoy other songs that have similar features.
- An **iterative, non-parametric and unsupervised learning method.**

### Dataset

Some songs share the same title while their ID in the dataset is different, so there are some situations in which the system will recommend multiple songs with the same title.

## Input Songs

To make this system customizable, you can modify the `input_songs.csv` file. The program will make recommendations base on this file.

## Spotify API

> We use the API to find the song which is not in our dataset.
> The recommender is build with K-Means algorithm.

The `.env` file need to be created by yourself.
You can copy the `.env.example` file and modify the content.
