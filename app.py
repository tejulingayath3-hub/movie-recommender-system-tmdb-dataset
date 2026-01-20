import streamlit as st
import pickle
import pandas as pd
import requests
import time

# 🔐 Load API key securely from Streamlit secrets
API_KEY = st.secrets["TMDB_API_KEY"]

# 🎬 Fetch poster with retries and error handling
def fetch_posters(movie_id, retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
            else:
                return None
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # exponential backoff
            else:
                st.warning(f"Poster fetch failed for movie ID {movie_id}: {e}")
                return None

# 🎥 Recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_posters(movie_id))
    return recommended_movies, recommended_movies_poster

# 📦 Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarty.pkl', 'rb'))

# 🌟 Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Choose a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            if posters[idx]:
                st.image(posters[idx])
            else:
                st.image("https://via.placeholder.com/200x300?text=No+Poster", caption="Poster not available")