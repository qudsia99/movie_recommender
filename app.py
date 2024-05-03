from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import numpy as np
import pandas as pd
import joblib
from rec_engine import get_recs 

# Creating flask instance
app = Flask(__name__)
Bootstrap(app)

# Loading engine and calling function
recommendation_engine = joblib.load('rec_engine.joblib')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def movies():
    movie_title = request.form.get('movie_title')
    movie_title = movie_title.lower()
    rec_df = pd.DataFrame({'title':[movie_title]})
    predictions = get_recs(movie_title)

    results = []
    for i in range(len(predictions)):
        result = { 'title': predictions['title'][i],
              'release_year': predictions['release_year'][i],
              'genre': predictions['genre_types'][i],
              'rating':predictions['rating'][i],
              'description': predictions['description'][i]}
        results.append(result)

    return render_template('index.html', result=result)

@app.route('/filter')
def diagnosis_page():
    return render_template('filter.html')

if __name__ == '__main__':
    app.run(debug=True)