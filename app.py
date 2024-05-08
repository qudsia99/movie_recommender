from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import pandas as pd
from rec_engine import get_recs 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Creating flask instance
app = Flask(__name__)
Bootstrap(app)

# Loading data 
df = pd.read_csv('cleaned_data/movie_data.csv')

# TF-IDF Vectorization to assess importance of each word in 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Measures similarity among movies based on their 'description' 
similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def movies():
    movie_title = request.form.get('movie_title')
    movie_title = movie_title.lower()

    movie_row = df[df['title'].str.lower() == movie_title]
    if movie_row.empty:
        return render_template('error.html',
        error_message=f"Movie '{movie_title}' not found in the dataset.")

    recommended_movies = get_recs(movie_title,df,similarity)
    results = recommended_movies.to_dict(orient='records')

    return render_template('index.html', results=results)

@app.route('/filter')
def diagnosis_page():
    return render_template('filter.html')

if __name__ == '__main__':
    app.run(debug=True)