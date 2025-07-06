# app.py
import os
import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# --- Load API key from config.json ---
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # if app.py is also in src/
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    OMDB_API_KEY = config["OMDB_API_KEY"]

except FileNotFoundError:
    st.error(
        "❌ `config.json` not found in src/. Please create it with your OMDB API key.")
    st.stop()
except KeyError:
    st.error("❌ 'OMDB_API_KEY' not found in config.json.")
    st.stop()

# --- Page Configuration ---
st.set_page_config(
    page_title="Movie Recommender 🎬",
    page_icon="🎥",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .movie-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
        }
        .plot-text {
            font-style: italic;
            color: #444;
            margin-bottom: 12px;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 30px;
            color: #222;
        }
        .recommend-title {
            font-size: 24px;
            font-weight: 600;
            margin-top: 40px;
            color: #1f77b4;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 6px;
            padding: 10px 20px;
            font-weight: bold;
            border: none;
        }
        .stSelectbox label {
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="header">🎬 Movie Recommender</div>',
            unsafe_allow_html=True)

# --- Movie Selection ---
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox(
    "Select a movie to get recommendations:", movie_list)

# --- Recommendation Button ---
if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)

        if recommendations is None or recommendations.empty:
            st.warning("Sorry, no recommendations found.")
        else:
            st.markdown(
                '<div class="recommend-title">🎯 Top Recommended Movies</div>', unsafe_allow_html=True)

            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if poster != "N/A":
                            st.image(poster, width=120)
                        else:
                            st.image(
                                "https://via.placeholder.com/120x180.png?text=No+Poster", width=120)

                    with col2:
                        st.markdown(
                            f'<div class="movie-title">{movie_title}</div>', unsafe_allow_html=True)
                        st.markdown(
                            f'<div class="plot-text">{plot}</div>' if plot != "N/A"
                            else "_Plot not available_", unsafe_allow_html=True
                        )
