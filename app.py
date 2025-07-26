import pickle
import streamlit as st
import requests
import os

def fetch_poster(movie_id):
    api_key = st.secrets["tmdb_api_key"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Image"
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

@st.cache_data(show_spinner="Downloading data...", max_entries=2)
def download_pickle_from_gdrive(file_id, filename):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    if not os.path.exists(filename):
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(r.content)
    with open(filename, 'rb') as f:
        return pickle.load(f)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

SIMILARITY_FILE_ID = "102huNjyF6_IIhDuR3HxX-oNsbFb6j9Y_"  # from Google Drive


with open('artifacts/movie_list.pkl', 'rb') as f:
    movies = pickle.load(f)


similarity = download_pickle_from_gdrive(SIMILARITY_FILE_ID, 'similarity.pkl')

st.header('🎬 Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
