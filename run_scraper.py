from wiki_scrape_db import get_headlines

headlines = []

for year in list(range(1995, 2020)):
    try:
        headlines.append(get_headlines(year))
    except Exception as e:
        print(e)

headlines.append(get_headlines(1994, start_month='July'))
headlines.append(get_headlines(2020, end_month='November'))

with open('headlines.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['day', 'month', 'year', 'subject', 'event', 'text'])
    csvwriter.writerows(list(chain(*headlines)))
