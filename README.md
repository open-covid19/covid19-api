<img src="https://user-images.githubusercontent.com/2068158/76208430-f1d45280-61ff-11ea-9115-9ecb77be8555.png" width="200" height="200" alt="Open-Covid19" />

![Testing](https://github.com/pascalwhoop/covid19-api/workflows/Testing/badge.svg)


- format with `black`
- packages with `poetry`
- requests with `requests` 
- api with `flask`
- data wrangling with `pandas`

should be pretty intuitive

to get requirements.txt for gcloud use `poetry export -f requirements.txt > requirements.txt`


Population data (population.csv) is from
https://data.worldbank.org/indicator/SP.POP.TOTL?end=2016&start=2016&view=bar
and I stored it as a gist to easily grab it via http call here 
https://gist.github.com/pascalwhoop/a38a70f1fc60711856ca2e6fea79e4e3
