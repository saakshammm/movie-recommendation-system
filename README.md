# 🎬 Movie Recommendation System

An interactive movie recommendation engine built using *Streamlit* and *user-based collaborative filtering*. It allows users to search for any movie and receive intelligent suggestions based on similarity with other users' preferences.

## 🔍 Features

- *Search any movie* by title
- *Get top 5 similar movie recommendations*
- Uses *collaborative filtering* based on user ratings
- Clean, intuitive UI powered by Streamlit

## 🧠 How It Works

This app:
- Loads movie metadata and ratings from main_data.csv
- Calculates *user similarity* using Pearson correlation
- Predicts top 5 movies based on nearest neighbors' preferences
- All logic is implemented in [recommendation-system.ipynb](https://github.com/saakshammm/movie-recommendation-system/blob/main/recommendation-system.ipynb)
- The front-end interface is built in [app.py](https://github.com/saakshammm/movie-recommendation-system/blob/main/app.py)

## 🛠 Tech Stack

- *Language*: Python
- *Libraries*: Pandas, NumPy, Streamlit, Scikit-learn
- *Interface*: Streamlit UI
- *Data*: Movie ratings & metadata in CSV

## 📦 Setup Instructions

1. *Clone the repo*:
   ```bash
   git clone https://github.com/saakshammm/movie-recommendation-system.git
   cd movie-recommendation-system

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Run the Streamlit app:

streamlit run app.py



Then open the provided URL (usually http://localhost:8501) in your browser.


## 🚀 Future Improvements
	•	Add content-based filtering (genre, description similarity)
	•	Deploy to Streamlit Cloud for public access
	•	Add user ratings input to personalize results
	•	Include movie posters and metadata from TMDB API

## 👤 Author

Saksham Kumar
