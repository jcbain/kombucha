# Kombucha

An experimental library for sentimental analysis.

## Datasets
- (hate speech Twitter sentiment analysis)[https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech?select=train.csv]
    - training set (31962)
    - unbalanced (class 0: 29720, class 1: 2242)
- (Sentiment140)[https://www.kaggle.com/kazanova/sentiment140]
    - 1.6 million labelled tweets
    - positive and negative and neutral
    - from 2009
- (Twitter US Airline Sentiment)[https://www.kaggle.com/crowdflower/twitter-airline-sentiment/]
    - 7000+ positive, negative, neutral classified tweets about 7 airlines
    - Doesn't contain tweet text, but does contain tweet id so should be able to back query

## For analysis

**Note**: this section needs to be moved into its own repository where the analysis actually occurs but for now it is a pin in a map of where we are going

#### Papers
[Going viral: How a single tweet spawned a COVID-19 conspiracy theory on Twitter](https://doi.org/10.1177%2F2053951720938405) Gruzd & Mai\

#### Tweets to collect 
- (1245104578087059467) One of the propogators of the #FilmYourHospital misinformation campaign
- (1374356089924247553) Tweet calling out Mississippi Health Department for telling an individual that there is not reported evidence that Moderna vaccine works


## Running

**from Docker**

This application can be run using `docker`. First, open a terminal and build an image

```sh
docker build -t <your-image-name> .
```

Then run the image with default `jupyter notebooks` running

```sh
docker run -it -p 8888:8888 -v $PWD/:/app -w /app <your-image-name>
```
