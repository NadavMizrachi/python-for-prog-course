import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_cars():
    df = pd.read_csv('../pandas_games/CARS1.csv')
    json = df.to_json()
    return json