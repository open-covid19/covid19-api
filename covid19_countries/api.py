from flask_api import FlaskAPI
from pathlib import Path
import pandas as pd
from joblib import Memory
from io import StringIO
from datetime import date, datetime
from flask import jsonify

memory = Memory("_cache")


app = FlaskAPI(__name__)

CONFIRMED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
DEATHS = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
RECOVERED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
POPULATIONS = "https://gist.githubusercontent.com/pascalwhoop/a38a70f1fc60711856ca2e6fea79e4e3/raw/0b45cceb7522e7eb7ac2219fb8f4421280949ea4/populations.csv"

@app.route('/api/deaths')
def deaths():
    return jsonify(fetch_data(DEATHS).to_dict(orient="records"))

@app.route('/api/confirmed')
def confirmed():
    return jsonify(fetch_data(CONFIRMED).to_dict(orient="records"))

@app.route('/api/recovered')
def recovered():
    return jsonify(fetch_data(RECOVERED).to_dict(orient="records"))

@app.route('/api/populations')
def populations():
    return jsonify(fetch_data(POPULATIONS).to_dict(orient="records"))

@memory.cache
def _fetch_data(url: str, d: datetime) -> pd.DataFrame:
    """
    cached request to github to avoid requesting this too often
    """
    return pd.read_csv(url).fillna(0)


def fetch_data(url: str) -> pd.DataFrame:
    now = datetime.now()
    cache_buster = datetime(year=now.year, month=now.month, day=now.day, hour=now.hour)
    return _fetch_data(url, cache_buster)


