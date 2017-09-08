import re
import requests
from datetime import datetime

from bs4 import BeautifulSoup
# https://www.dataquest.io/blog/web-scraping-tutorial-python/

from .models import Comic


def _solve_day_format(s):
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)


class NewComicsParser(object):
    name = 'new_comics_spider'
    domain = 'http://leagueofcomicgeeks.com'
    base_url = 'http://leagueofcomicgeeks.com/comics/new-comics'

    def parse(self, date):
        url = self.base_url

        year, month, day = date.split('-')
        url = '{url}/{year}/{month}/{day}'.format(
            url=url,
            year=year,
            month=month,
            day=day,
        )

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        weekly_index = 0
        for comic in soup.select('#comic-list li.media'):
            external_id = comic['id'].replace('comic-', '')
            title = comic.select('.comic-title a')[0].get_text()

            details = comic.select('.comic-details')[0].get_text().split(' \xa0·\xa0 ')

            publisher = ''
            if len(details) > 0:
                publisher = details[0]

            release_date = ''
            if len(details) > 1:
                release_date = details[1]
                release_date = _solve_day_format(release_date)
                release_date = datetime.strptime(release_date, '%b %d, %Y')

            price = ''
            if len(details) > 2:
                price = details[2]

            description = comic.select('.comic-description p')[0].get_text()
            description = description.replace('View »', '')
            cover_url = comic.select('.comic-cover-art img')[0]['data-original']
            cover_url = cover_url.replace('/medium/', '/large/')
            cover_url = '{}{}'.format(self.domain, cover_url)

            comic, _ = Comic.objects.get_or_create(external_id=int(external_id))
            comic.title = title
            comic.publisher = publisher if publisher else ''
            if release_date == '':
                release_date = date
            comic.release_date = release_date
            comic.price = price
            comic.description = description
            comic.cover_url = cover_url
            comic.weekly_index = weekly_index
            comic.save()
            weekly_index += 1
