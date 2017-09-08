from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from dashboard.utils import (
    get_closest_wednesday_date,
    get_closest_wednesday_from_date,
)


class ComicsManager(models.Manager):
    def _get_closest_wednesday_from_date(self, date=None):
        if date is None:
            return get_closest_wednesday_date()
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            return get_closest_wednesday_from_date(date)
        except ValueError as e:
            return get_closest_wednesday_date()

    def nearest_wednesday_comics(self, date=None):
        return self.filter(release_date=self._get_closest_wednesday_from_date(date))

    def tracked_by_user(self, user, date=None):
        return self.filter(tracked_by=user, release_date=self._get_closest_wednesday_from_date(date))


class Comic(models.Model):
    external_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=512, blank=True)
    publisher = models.CharField(max_length=512, blank=True)
    release_date = models.DateField(blank=True, null=True)
    price = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True)
    cover_url = models.CharField(max_length=512, blank=True)
    weekly_index = models.IntegerField(blank=True, null=True)

    tracked_by = models.ManyToManyField(User, related_name='tracked_comics')

    objects = ComicsManager()

    class Meta:
        ordering = ['-release_date', 'weekly_index']

    def __str__(self):
        return '{}, {}'.format(self.title, self.release_date)
