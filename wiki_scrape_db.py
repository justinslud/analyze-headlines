import requests
import postgres
from bs4 import BeautifulSoup
# from .. import logger

# connect db

# get cursor


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

years = range(1995, 2020)

headers = {}

for years in years:
    get_current_events(year)

get_current_events(1994, start_month='July')
get_current_events(2020, end_month='November')

# day_month_years = c.execute('SELECT DISTINCT CONCAT(day, month, year) as month_year from headlines').fetchall()

# sections = c.execute('SELECT subject from subjects').fetchall()

def get_current_events(year=2020, start_month='January', end_month='December', start_day=1):

    for month in months[months.index(start_month): months.index(end_month)+1]:

        # if '{}{}'.format(month, year) not in month_years:
        response = requests.get('https://en.wikipedia.org/wiki/Portal:Current_events/{month}_{year}', headers=headers)

        if response.status == 200:

            soup = BeautifulSoup(response.content)

            try:
                get_headlines(soup, month, year)

                # logger.debug(f'Scraped {month} {year}')

            except Exception:
                # logger.warning(f'Could not scrape {month} {year}. {Exception}')
                pass

def get_headlines(soup, month, year):

    for day, body in enumerate(soup.find_all('td', {'class': 'description'})):

        for section in body.find_all('td')

            # subject = section.

            # if subject not in subjects:
                # c.execute('INSERT INTO subjects VALUES({}. {})'.format(len(sections), subject))

            for headline in section.find_all('li'):

                subheadlines = headline.find_all('li')

                if subheadlines:
                    event = headline.a.text

                    for subheadline in subheadlines:
                        text = subheadline.text

                        # c.execute('INSERT INTO headlines VALUES({}, {}, {}, {})'.format(day, month, year, section, text))  


                else:
                    event = 'NULL'
                text = headline.text


                # c.execute('INSERT INTO headlines VALUES({}, {}, {}, {})'.format(day, month, year, section, text))  

                # c.commit()  

