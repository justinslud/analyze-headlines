import streamlit as st
import numpy as np
import pandas as pd
import requests

import matplotlib.pyplot as plt
import bokeh
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


st.title('Wikipedia Current Events Analysis')

option = st.sidebar.selectbox('Tab', ['Trend Plot', 'Predict Subject'])

headlines = pd.read_csv('data/1995-2017clean.csv')

@st.cache
def predict_subject(headline):
    return requests.get('http://127.0.0.1:5000/', json={'headline': headline}).json()

@st.cache
def keyword_counts(keyword):
    matches = headlines[(headlines.text.str.contains(keyword)) | (headlines.event.str.contains(keyword))].drop('day', axis=1)
    counts = matches.groupby('year').text.count()
    return counts

def trend_plot(keyword):
    counts = keyword_counts(keyword)
    cds = ColumnDataSource(pd.DataFrame(data=counts))
    p = figure(plot_width = 400, plot_height = 400, tools='hover', tooltips='@text', title = 'Wikipedia Current News mentions for {}'.format(keyword))
    p.line(counts.index, counts.values)

    p.circle('year', 'text', size=5, fill_color='grey', fill_alpha=.4, \
             hover_color='lightblue', hover_alpha=.2, source=cds)

    return p
                                        

if option == 'Predict Subject':

    st.write('Predict Subject')

    default_headline = 'Usain bolt wins the 100 meter dash in the London 2012 Olympics.'

    headline = st.text_input('Your headline', default_headline)

    try:
        response = predict_subject(headline)

        subject = response['subject']

        st.write('Predicted Subject:', subject)

        probs = response['all_proba']

        proba = pd.Series(probs)
        
        # st.bar_chart(proba.sort_values(ascending=False))

        p = figure(plot_height=250, title="Subject Probabilities")
        p.hbar(y=list(range(9)), height=list(proba.values))
        p.x_range(0, 1)

        st.bokeh_chart(p)

    except:
        pass


elif option == 'Trend Plot':

    st.write('Trend Plot')

    default_keyword = 'Tom Brady'

    keyword = st.text_input('Your keyword', default_keyword)


    try:
        # counts = keyword_counts(keyword)

        # st.line_chart(counts)
        # st.write(counts)
        # fig, ax = plt.subplots()
        # counts.plot(kind='line', color='k', ax=ax)
        # # plt.ylim((-.5, counts.max()+.5))
        # # # min, max = counts.index.min(), counts.index.max() + 1
        # # min, max = 2007, 2017
        # # increment = 1 if (max - min) < 10 else 2
        # # plt.xticks(range(min, max, increment), rotation=45)
        # plt.title(keyword.title() + ' Trend Plot')
        # # ax.xlabel('Year')
        # ax.ylabel('Mentions')
        # st.pyplot(fig)

        st.bokeh_chart(trend_plot(keyword))

    except:
        pass
# chart_data = pd.DataFrame(data=[[1,2], [4,5]], columns=['option1', 'option2'])

# try:
#     st.line_chart(chart_data[option])
# except:
#     pass

# print(option) # whatever is chosen

# st.sidebar.selectbox(same thing)

