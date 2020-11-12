import requests
import bs4
from bs4 import BeautifulSoup
import re
import csv
import time
import random
from itertools import chain

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def get_headlines(year=2020, start_month='January', end_month='December', months_list=None):

    headlines = []

    if months_list is None:
        months_list = months[months.index(start_month): months.index(end_month)+1]

    for month in months_list:

        time.sleep(5 + random.random())
        url = f'https://en.wikipedia.org/wiki/Portal:Current_events/{month}_{year}'
        
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            try:
                headlines.append(get_month_headlines(soup, month, year))
                print(f'Scraped {len(headlines[-1])} headlines from {month} {year}')

            except Exception as e:
                print(e)

    return list(chain(*headlines))

def get_month_headlines(soup, month, year):

    headlines = []

    for day, div in enumerate(soup.find_all('div', {'id': re.compile(r'{}_{}_\d\d'.format(year, month))})):

        for element in div.next_elements:
            
            if type(element) == bs4.NavigableString:
                continue

            if element.name == 'div':
                break

            if element.name == 'td' and element.next_element.name == 'ul':
                for headline in element.next_element.find_all('li'):                              
                    text = headline.text
                    headlines.append([day+1, month, year, None, None, text])

            if element.name == 'table':
                td = element.find('td', {'class': 'description'})
                if td:
                    if td.ul:
                        for headline in element.find('td', {'class': 'description'}).ul.find_all('li'):
                            text = headline.text
                            headlines.append([day+1, month, year, None, None, text])

            # subject
            if element.name == 'dt':

                subject = element.text
                
                for next_element in element.next_elements:
                    
                    if type(next_element) == bs4.NavigableString:
                        continue

                    if next_element.name not in ['ul', 'li', 'a', 'b', 'i']:
                        break

                    # checks if event present
                    if next_element.name == 'ul':

                        # find all events
                        subheadlines = next_element.find_all('li')

                        if subheadlines:
     
                            # loop through events
                            for subheadline in subheadlines:
                                event = subheadline.a.text

                                # checks for multiple headlines within an event
                                if subheadline.ul:

                                    # loops through headlines for a specific event
                                    for headline in subheadline.ul.find_all('li'):
                               
                                        text = headline.text
                                        headlines.append([day+1, month, year, subject, event, text])
                            

                    elif next_element.name == 'li':
                        event = None
                        text = next_element.text

                        headlines.append([day+1, month, year, subject, event, text])

    return headlines