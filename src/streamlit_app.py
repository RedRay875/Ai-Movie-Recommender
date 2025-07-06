# app.py
import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# Load API key from config
config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

# Page configuration
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
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 20px;
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
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: bold;
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
                        st.markdown(f'<div class="plot-text">{plot}</div>' if plot !=
                                    "N/A" else "_Plot not available_", unsafe_allow_html=True)
