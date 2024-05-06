# Import Dependencies
from pathlib import Path
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib

# Filter Warnings
from warnings import filterwarnings

df = pd.read_csv('cleaned_data/movie_data.csv')

# TF-IDF Vectorization to assess importance of each word in 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Measures similarity among movies based on their 'description' 
similarity = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_recs(movie_title, df, similarity, columns=['title', 'release_year', 'genre_types', 'description', 'rating', 'original_title']):
 
    # Filter movies based on release year and genre
    idx = df[df['title'] == movie_title].index
    if idx.empty:
        return f"Movie '{movie_title}' not found in the dataset."

    # Get the first index from the list (assuming there's only one match)
    idx = idx[0]

    # Get similarity scores of all movies with the given movie
    sim_scores = list(enumerate(similarity[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 similar movies (excluding the given movie itself)
    sim_scores = sim_scores[1:11]

    # Get indices of the top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]

    # Get DataFrame of recommended movies with specified columns
    recommended_movies = df.iloc[movie_indices][columns]

    return recommended_movies

# recommended_movies = get_recs('insidious',df, similarity)
# print(recommended_movies)

# Save the function to a joblib file
joblib.dump(get_recs, 'rec_engine.joblib')