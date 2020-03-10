from flask_api import FlaskAPI
from pathlib import Path
import pandas as pd
from io import StringIO
from datetime import date, datetime
from flask import jsonify, Response, redirect
from flask_cors import CORS
from covid19_countries.utils import recursive_camel_case
import functools



app = FlaskAPI(__name__)
CORS(app)

CONFIRMED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
DEATHS = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
RECOVERED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
POPULATIONS = "https://gist.githubusercontent.com/pascalwhoop/a38a70f1fc60711856ca2e6fea79e4e3/raw/0b45cceb7522e7eb7ac2219fb8f4421280949ea4/populations.csv"

@app.route('/')
def root():
    return redirect("https://github.com/open-covid19/covid19-api", 302)

@app.route('/v1/deaths')
def deaths():
    """
    returns the deaths count data provided by CSSE of John Jopkins, proxied within the last 1h and converted to JSON
    """
    return fetch_and_clean_csv(DEATHS)

@app.route('/v1/confirmed')
def confirmed():
    """
    returns the confirmed count data provided by CSSE of John Jopkins, proxied within the last 1h and converted to JSON
    """
    return fetch_and_clean_csv(CONFIRMED)

@app.route('/v1/recovered')
def recovered():
    """
    returns the recovered count data provided by CSSE of John Jopkins, proxied within the last 1h and converted to JSON
    """
    return fetch_and_clean_csv(RECOVERED)

@app.route('/v1/populations')
def populations():
    """
    returns the populations count per country as published by the world bank. This data is static. 
    """
    return fetch_and_clean_csv(POPULATIONS)


@functools.lru_cache(maxsize=1)
def _fetch_data(url: str, d: datetime) -> pd.DataFrame:
    """
    cached request to github to avoid requesting this too often
    """
    return pd.read_csv(url).fillna(0)


def fetch_data(url: str) -> pd.DataFrame:
    now = datetime.now()
    cache_buster = datetime(year=now.year, month=now.month, day=now.day, hour=now.hour)
    return _fetch_data(url, cache_buster)

def fetch_and_clean_csv(url: str) -> Response:
    data = fetch_data(url).to_dict(orient="records")
    cleaned = recursive_camel_case(data)
    return cleaned
