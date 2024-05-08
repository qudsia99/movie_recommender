# Importing Dependencies
from pathlib import Path
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib

# Filter Warnings
from warnings import filterwarnings

df = pd.read_csv('cleaned_data/movie_data.csv')

# TF-IDF Vectorization to assess importance of each word in the 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Measuring similarity (cosine matrix) among movies : 'combined' feature
similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

# Building the function
def get_recs(movie_title, df, similarity, columns=['title', 'release_year', 'genre_types', 'description', 'rating', 'original_title']):
 
    # Searching inputted movie in dataset
    idx = df[df['title'] == movie_title].index
    if idx.empty:
        return f"Movie '{movie_title}' not found in the dataset."

    # Grabbing the first index from the list 
    idx = idx[0]

    # Fetching similarity scores of corresponding movies
    sim_scores = list(enumerate(similarity[idx]))

    # Sorting the movies based on similarity scores using lambda
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Grabbing first 10 and indices
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    # Filtering dataframe with the recommended movies 
    recommended_movies = df.iloc[movie_indices][columns]

    return recommended_movies

# Incase to debug, unhash lines 48-49
# recommended_movies = get_recs('insidious',df, similarity)
# print(recommended_movies)
