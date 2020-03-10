<p align="center">
  <a href="https://github.com/open-covid19/covid19-api">
    <img src="https://data.remondevries.com/openconvid19/logo.svg" alt="Bootstrap logo" width="72" height="72">
  </a>
</p>

<h2 align="center">Bootstrap</h2>

![Testing](https://github.com/pascalwhoop/covid19-api/workflows/Testing/badge.svg)
[![Join the chat at https://gitter.im/open-covid19/community](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/open-covid19/community)

---

# Instructions

This goal of this project is to serve an API serving trusted data to a large base of consumers. To do this, we consume the data from upstream sources such as the WHO or John Hopkins. After a bit of cleaning and making the data more uniform, we then expose it as a REST API.

## Current state

- backend hosted by AppEngine, proxying data from CSSE and worldbank
- built by github actions and deployed on push to master

## Goal state

- all data in Firebase and DB exposed as read only to the world
- ETL pipelines which take data from upstream sources and write them to firebase (potentially with a middle step through BigQuery)

## Facts 

- Format with `black`
- Packages with `poetry`
- Requests with `requests` 
- API with `flask`
- data wrangling with `pandas`

_Should be pretty intuitive._

---

To get requirements.txt for gcloud use `poetry export -f requirements.txt > requirements.txt`

## Data Sources

Population data (population.csv) is from [data.worldbank.org](https://data.worldbank.org/indicator/SP.POP.TOTL?end=2016&start=2016&view=bar)

Stored it as a gist to grab it easily via `http call` here [gist.github.com](https://gist.github.com/pascalwhoop/a38a70f1fc60711856ca2e6fea79e4e3)
