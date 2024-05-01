from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import numpy as np
import pandas as pd

# Creating flask instance
app = Flask(__name__)
Bootstrap(app)

# Preloading column names
# column_names = ['titl']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['POST'])
def movies():
    movie_title = request.form.get('title')
    rec_df = pd.DataFrame([movie_title])
    prediction = model.predict(rec_df)
    result = prediction['title']
    return render_template('index.html', result=result)

@app.route('/filter')
def diagnosis_page():
    return render_template('filter.html')




if __name__ == '__main__':
    app.run(debug=True)