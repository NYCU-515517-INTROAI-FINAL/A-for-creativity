# A-for-creativity

## Environment

---

- Python 3.11.3

## Package Dependencies

---

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

---

## K-Means

---

### Dataset

Some song's names are the same while their ID in the dataset is different,
so there are some situations in which it will recommend multi-song where information is the same.

## Input Songs

You can modify the `input_songs.csv` file.
The program will base on this file to make recommendations.

## Spotify API

> We use the API to find the song which is not in our dataset.
> The recommender is build with K-Means algorithm.

The `.env` file need to be create by yourself.
You can copy the `.env.example` file and modify the content.
