🎬 Movie Recommendation System – Streamlit Project

📌 About the Project

This is a content-based movie recommendation system built using Python.
The application recommends movies similar to a selected movie based on genres, overview, cast, and crew.
The project is developed in Jupyter Notebook and deployed as an interactive Streamlit web application.

🎯 Project Goals

Recommend similar movies based on content

Understand relationships between movies using text features

Apply cosine similarity for recommendations

Deploy the model as a user-friendly web app

🛠 Tools Used

Python

Pandas & NumPy

Scikit-learn

Streamlit

Pickle

TMDB API

🔄 Data Cleaning & Preparation

Merged movies and credits datasets

Removed unnecessary columns

Handled missing values

Extracted key features (genres, keywords, cast, crew, overview)

Combined features into a single text column

Converted text data into vectors using CountVectorizer

📊 Recommendation Highlights

Content-based filtering approach

Cosine similarity used to find similar movies

Top 5 movie recommendations for each selection

Movie posters fetched dynamically using TMDB API

Secure API key handling using Streamlit secrets

▶️ How to Run This Project

Install required Python libraries

Add your TMDB API key in Streamlit secrets

Run the Streamlit app using streamlit run app.py

Select a movie and view recommendations
