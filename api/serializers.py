from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers

from dashboard.models import Comic


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'tracked_comics')


class ComicSerializer(serializers.ModelSerializer):
    external_url = serializers.SerializerMethodField()
    tracked_by = serializers.SerializerMethodField()
    is_tracked = serializers.SerializerMethodField()

    class Meta:
        model = Comic
        fields = (
            'pk',
            'external_id',
            'title',
            'publisher',
            'release_date',
            'price',
            'description',
            'cover_url',
            'weekly_index',
            'external_url',
            'tracked_by',
            'is_tracked',
        )

    def __init__(self, *args, **kwargs):
        super(ComicSerializer, self).__init__(*args, **kwargs)
        self.user = self.context.get('request').user

    def get_external_url(self, obj):
        return 'https://leagueofcomicgeeks.com/comic/{}/{}'.format(obj.external_id, slugify(obj.title))

    def get_tracked_by(self, obj):
        return [u.username for u in obj.tracked_by.all()]

    def get_is_tracked(self, obj):
        if self.user is not None:
            return self.user in obj.tracked_by.all()
        return False
