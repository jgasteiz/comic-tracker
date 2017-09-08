from datetime import timedelta

from django.core.management.base import BaseCommand
from dashboard.scrapers import NewComicsParser
from dashboard.utils import get_closest_wednesday_date


class Command(BaseCommand):
    help = 'Fetch comics from next 10 weeks'

    def handle(self, *args, **options):
        date_list = []
        closest_wednesday = get_closest_wednesday_date()
        date_list.append(str(closest_wednesday))

        # Add the next few Wednesdays after the closest one.
        next_wednesday = closest_wednesday
        for i in range(0, 10):
            next_wednesday = next_wednesday + timedelta(days=7)
            date_list.insert(0, str(next_wednesday))

        # Fetch comics for the next weeks
        parser = NewComicsParser()
        for date in date_list:
            parser.parse(date=date)
