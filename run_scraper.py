from wiki_scrape_db import get_healines

headlines = []

for year in [2003, 2004, 2005, 2006]:
    try:
        headlines.append(get_headlines(year))
    except Exception as e:
        print(e)

with open('headlines.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['day', 'month', 'year', 'subject', 'event', 'text'])
    csvwriter.writerows(list(chain(*headlines)))
