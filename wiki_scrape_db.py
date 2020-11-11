import requests
import bs4
from bs4 import BeautifulSoup
# import psycopg2
# import credentials as creds
import re
import csv
import time
import random

# conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER +" password="+ creds.PGPASSWORD
# conn = psycopg2.connect(conn_string)

# c = conn.cursor()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

years = range(1995, 2020)

headers = {}

# for years in years:
#     get_current_events(year)

# get_current_events(1994, start_month='July')
# get_current_events(2020, end_month='November')

# day_month_years = c.execute('SELECT DISTINCT CONCAT(day, month, year) as month_year from headlines').fetchall()

# sections = c.execute('SELECT subject from subjects').fetchall()

def get_headlines(year=2020, start_month='January', end_month='December'):

    headlines = []

    for month in months[months.index(start_month): months.index(end_month)+1]:

        time.sleep(5 + random.random())

        response = requests.get('https://en.wikipedia.org/wiki/Portal:Current_events/{month}_{year}', headers=headers)

        if response.status == 200:

            soup = BeautifulSoup(response.content)

            try:
                headlines.append(get_headlines(soup, month, year))

            except:
                pass

    return rows

def get_month_headlines(soup, month, year):

    headlines = []

    for day, div in enumerate(soup.find_all('div', {'id': re.compile(r'{}_{}_\d\d'.format(year, month))})):
        
        for element in div.next_elements:
            
            if type(element) == bs4.NavigableString:
                continue

            if element.name == 'div':
                break

            if element.name == 'dt':

                subject = element.text
                
                for next_element in element.next_elements:
                    
                    if type(next_element) == bs4.NavigableString:
                        continue

                    if next_element.name not in ['li', 'ul', 'a', 'i', 'b']:
                        break

                    # print(next_element.a.text)
                    if next_element.name == 'ul':

                    
                        subheadlines = next_element.find_all('ul')

                        if subheadlines:

                            event = next_element.a.text
                            # print(event)
                            # print(event, subheadlines)
                            for subheadline in subheadlines:

                                text = subheadline.text
                                headlines.append([day+1, month, year, subject, event, text])
                        

                        else:
                            event = None
                            text = next_element.text

                            headlines.append([day+1, month, year, subject, event, text])

    return headlines
# get_headlines(year=2020, start_month='November', end_month='November')

soup = BeautifulSoup(open('february_2015.html', 'r'), 'html.parser')

headlines = get_month_headlines(soup, 'February', 2015)

# with open('february_2015.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(['day', 'month', 'year', 'subject', 'event', 'text'])
#     csvwriter.writerows(headlines)

# with open('headlines.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(['day', 'month', 'year', 'subject', 'event', 'text'])
#     for i in headlines:
#         csvwriter.writerows(i)