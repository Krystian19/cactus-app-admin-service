from django.db import models
from rest_framework import serializers
from .models import Language
from .models import Anime
from .models import Genre
from .models import Season
from .models import SeasonGenre
from .models import SeasonDescription
from .models import SeasonAlternativeTitle
from .models import Episode
from .models import EpisodeVersion


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


class SeasonGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonGenre
        fields = ('id',
                  'season_id',
                  'genre_id',
                  'created_at',
                  'updated_at')


class SeasonDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonDescription
        fields = ('id',
                  'season_id',
                  'language_id',
                  'language_id',
                  'created_at',
                  'updated_at')


class SeasonAlternativeTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonAlternativeTitle
        fields = ('id',
                  'season_id',
                  'title',
                  'created_at',
                  'updated_at')


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('id',
                  'episodeOrder',
                  'thumbnail',
                  'created_at',
                  'updated_at')


class EpisodeVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EpisodeVersion
        fields = ('id',
                  'episode_url',
                  'episode_id',
                  'language_id',
                  'title',
                  'created_at',
                  'updated_at')
