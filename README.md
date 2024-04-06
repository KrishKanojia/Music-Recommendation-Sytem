**Spotify Music Recommendation System**

This project explores building a music recommendation system leveraging Spotify's API.

**Project Goals**

Recommend music to users based on two scenarios:

1. **Similar New Releases**: Recommend new songs similar to the user's listening preferences.
2. **Content-Based Recommendation**: Recommend songs based on audio features (genre, tempo, mood) that align with the user's favorites.

Control the trade-off between these recommendations using a hyperparameter - Alpha.

- Higher Alpha values prioritize new releases.
- Lower Alpha values prioritize content-based recommendations.

**Functionality Overview**

*repository.py*:

- Obtains a Spotify access token for API interaction.
- Retrieves trending playlists using the Spotify API.

*app.ipynb*:

- This Jupyter Notebook is the core of the recommendation system.

**How to Use This Project**

**Prerequisites:**

1. Python 3.x with necessary libraries (e.g., Spotipy)
2. A Spotify Developer Account and Access Token (instructions can be found on the Spotify Developer website)

**Instructions:**

1. Clone this repository.
2. Install dependencies. Run `pip install -r requirements.txt`.
3. Configure access token. Replace the placeholder in `repository.py` with your actual Spotify access token.
4. Run the Jupyter Notebook. Open `app.ipynb` in your Jupyter Notebook environment.
