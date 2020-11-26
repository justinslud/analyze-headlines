# scrape-wikipedia-current-events

Please see the general info for this project on the [Projects page](https://justinslud.github.io/projects.html##wikipedia-current-events-analysis)
 
I split this project into 5 parts. The links are to the scripts and notebooks within this repository.

1. [Collecting the data](https://github.com/justinslud/scrape-wikipedia-current-events/blob/main/1_scrape_headlines.py)
2. [Exploring and understanding the data](https://github.com/justinslud/scrape-wikipedia-current-events/blob/main/2_explore_data.ipynb)
3. [Machine learning modelling](https://github.com/justinslud/scrape-wikipedia-current-events/blob/main/3_model_subject.ipynb)
4. [Building a Flask API](https://github.com/justinslud/scrape-wikipedia-current-events/blob/main/4_make_api.py)
5. [Making an interactive Streamlit app](https://github.com/justinslud/scrape-wikipedia-current-events/blob/main/5_build_interface.py)

You can access the Streamlit app [here](https://share.streamlit.io/justinslud/streamlit-apps/main/app.py) and clicking 'Wikipedia Current Events Analysis' on the sidebar.

Here are a summary and notes on how I carried out the project:

## 1. Collecting the data

The Wikipedia current events portal has changed their HTML structure over the years. Despite not scraping all headlines, I still scraped over 50,000 headlines from 1995-2017.

<br>

## 2. Exploring and understanding the data

I try and plot how often a term appears in headlines over the years, but this is not a good measure of how popular a term actually is. Wikipedia is heavily biased towards specific people and certain types of events. If I wanted to do an actual trend plot, my dataset of choice would be a media website, but even those are biased towards certain people and events.

<br>

## 3. Exploring and understanding the data

Since this project was more exploratory, I did not have a specific prediction task in mind. I tried to predict which year a headline was from through KMeans clustering and logistic regression, but the heavy class imbalance (only 200 articles from 1995 but 2000 from 2015) made the task difficult.

Predicting the subject of headlines was a more interesting and successful task. I had to reduce the number of possible categories to 9 by combining subjects. The logistic regression model had an average recall of .7, which is faily accurate considering a headline could be strongly related to 2 or more categories.

<br>

## 4. Building a Flask API

I wanted to build an example API where a user could send headlines and receive my model's predictions and calculated probabilities. The actual prediction is taken care of by sci-kit, so the challenge here came from structuring the response JSON, handling 1 or many inputs, and handling errors.

<br>

## 5. Making an interactive Streamlit app

The trend plotting exploratory data analysis and subject prediction look better with visuals on a website. Streamlit made this really straightforward and I used bokeh to make the trend plot.