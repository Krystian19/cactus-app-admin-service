from django.db import models
from rest_framework import serializers
from .models import Language
from .models import Anime
from .models import Episode
from .models import Genre
from .models import Season


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'iso_code', 'created_at', 'updated_at')


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'title', 'created_at', 'updated_at')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'thumbnail', 'created_at', 'updated_at')


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Season
            fields = ('id',
                      'anime_id',
                      'seasonOrder',
                      'title',
                      'startedAiring',
                      'stoppedAiring',
                      'poster',
                      'background',
                      'created_at',
                      'updated_at')


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'episodeOrder', 'thumbnail',
                  'created_at', 'updated_at')
