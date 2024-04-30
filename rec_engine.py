# Import Dependencies
from pathlib import Path
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Filter Warnings
from warnings import filterwarnings

# Loading cleaned data
df_path = Path('cleaned_data/movie_data.csv')
df = pd.read_csv(df_path)

# TF-IDF Vectorization to assess importance of each word in 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Measures similarity among movies based on their 'description' 
similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

# Creating function to find similar movies based on movie name given
def get_recs(title,similarity=similarity):
    movie_index = df[df['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with the given movie
    sim_scores = list(enumerate(similarity[movie_index]))

    # Sorting the movies based on the similarity scores, in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # grabbing top 10 similar movies
    sim_scores = sim_scores[1:11]
    # getting movie indices
    movie_indices = [i[0] for i in sim_scores]

    # return top 10 movies
    return df['title'].iloc[movie_indices]
    #recs = [(df['title'].iloc[i], score) for i, score in sim_scores]
    #return recs
    
# Printing Recommendations
print(get_recs('Insidious'))
