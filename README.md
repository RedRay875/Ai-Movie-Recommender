# 🎬 AI Movie Recommender System

An intelligent movie recommender system built with Python, Pandas, and Streamlit, powered by content-based filtering. Users can select a movie and receive similar recommendations along with their plot summaries and posters using the OMDb API.

---

## 🚀 Features

- 🎞️ Content-based movie recommendations
- 🧠 Machine learning-powered similarity scoring
- 🧾 Movie plot and poster via OMDb API
- 🎨 Clean and modern Streamlit UI
- 📦 Modular code structure (`src/`, `recommend.py`, `omdb_utils.py`)

---

## Download Dataset 
https://www.kaggle.com/datasets/harshshinde8/movies-csv

## 📁 Project Structure
│
├── src/
│ ├── main.py # Entry point for the app (Streamlit UI)
│ ├── config.json # Stores OMDb API key
│ ├── movies.csv # Dataset used for recommendation
│ ├── omdb_utils.py # Fetches plot and poster using OMDb API
│ ├── preprocess.py # Data cleaning or feature extraction
│ ├── recommend.py # Core recommendation logic
│ └── start_app.txt # Optional launcher description or usage note
│
├── .gitignore # Files/directories to ignore in version control
├── Movie_recommendation_system.ipynb # Notebook version for exploration
├── requirements.txt # Python dependencies
└── README.md # Project documentation
