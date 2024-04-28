from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import numpy as np
import pandas as pd

# Creating flask instance
app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html')















if __name__ == '__main__':
    app.run(debug=True)