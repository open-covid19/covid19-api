# %% [markdown]

# A small notebook to map the progress of each countries infection rate in relation to its population. 
# The idea is to normalize the infection rate by its population to be able to compare large and small countries.
# This way one can get a feel of the "concentration" of infected people per country

# %%

from pathlib import Path
import pandas as pd
import requests
from joblib import Memory
from io import StringIO
from datetime import date, datetime

memory = Memory("_cache")

# %%

CONFIRMED = "https://quixotic-elf-256313.appspot.com/api/confirmed"


@memory.cache
def _fetch_data(url: str, d: datetime) -> pd.DataFrame:
    """
    cached request to github to avoid requesting this too often
    """
    return pd.read_json(url)


def fetch_data(url: str) -> pd.DataFrame:
    now = datetime.now()
    cache_buster = datetime(year=now.year, month=now.month, day=now.day, hour=now.hour)
    return _fetch_data(url, cache_buster)




# %%
df = fetch_data(CONFIRMED).transpose()
df.columns = df.loc["Country/Region"]
df = df.drop(["Province/State", "Country/Region", "Lat", "Long"]).groupby(df.columns, axis=1).sum().fillna(0)
df.index = pd.to_datetime(df.index)

# %% 
# west Only
df_west = df[["Germany", "Italy", "France", "Spain", "Belgium", "Netherlands", "UK", "US"]]
#df_eu.plot(logy=True)
df_west.plot(logy=True, figsize=[12,12])
df_west.plot( figsize=[12,12])

# %%

with open(Path("COVID-19") / "csse_covid_19_data" / "csse_covid_19_time_series" / "time_series_19-covid-Confirmed.csv") as f:
    df = pd.read_csv(f)


# %% 
df
# %%

df_trans = (df
    .drop(columns=["Province/State", "Lat", "Long"])
    .set_index("Country/Region")
    .transpose()
    # .Index.astype("date")
    .rename(columns={"Country/Region": "date"})
    # .groupby(df.columns, axis=1)
    # .sum()
    # .drop([columns=["Mainland China"]])
)
df_trans

# %%

(df_trans
    .groupby(df_trans.columns, axis=1)
    .sum()
    .drop(columns=["Mainland China"])
    # .plot(logy=True)
    .plot()
    # .drop([columns=["Mainland China"]])
)
