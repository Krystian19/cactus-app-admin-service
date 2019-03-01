from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from functools import reduce
import operator

from Anime.serializers import LanguageSerializer
from Anime.serializers import AnimeSerializer
from Anime.serializers import GenreSerializer
from Anime.serializers import SeasonSerializer
from Anime.serializers import SeasonGenreSerializer
from Anime.serializers import SeasonDescriptionSerializer
from Anime.serializers import SeasonAlternativeTitleSerializer
from Anime.serializers import EpisodeSerializer
from Anime.serializers import EpisodeVersionSerializer

from .models import Language
from .models import Anime
from .models import Genre
from .models import Season
from .models import SeasonGenre
from .models import SeasonDescription
from .models import SeasonAlternativeTitle
from .models import Episode
from .models import EpisodeVersion


def filter_title_string(search_params):
    """
    Filter based on a provided List of Strings, returns operator only useful 
    for a "title" field.
    """
    # Filter list of elements based on the string sent as params
    return reduce(operator.and_, [Q(title__icontains=s) for s in search_params])


def filter_by_gender(genre_id_list):
    """
    Filter based on a provided List of Integers corresponding to a ids of Genre Models.
    """
    # Filter list of elements based on the string sent as params
    return reduce(operator.and_, [Q(seasongenre__genre_id=int(genre)) for genre in genre_id_list])

# Create your views here.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def get_queryset(self):
        queryset = Season.objects.all()

        # When the title filter is present, is a string of strings separated by + signs
        title_param = self.request.query_params.get('title', None)
        if title_param is not None:
            parsed_title_params = title_param.split(' ')

            queryset = queryset.filter(
                filter_title_string(parsed_title_params))

        # When the Genre filter is present, is a string of integers separated by commas
        genres_param = self.request.query_params.get('genres', None)
        if genres_param is not None:
            parsed_genres_params = genres_param.split(',')

            # Apply filter for every genre in sequentially
            for genre_param in parsed_genres_params:
                queryset = queryset.filter(
                    filter_by_gender([genre_param]))

        return queryset


class SeasonGenreViewSet(viewsets.ModelViewSet):
    queryset = SeasonGenre.objects.all()
    serializer_class = SeasonGenreSerializer


class SeasonDescriptionViewSet(viewsets.ModelViewSet):
    queryset = SeasonDescription.objects.all()
    serializer_class = SeasonDescriptionSerializer


class SeasonAlternativeTitleViewSet(viewsets.ModelViewSet):
    queryset = SeasonAlternativeTitle.objects.all()
    serializer_class = SeasonAlternativeTitleSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class EpisodeVersionViewSet(viewsets.ModelViewSet):
    queryset = EpisodeVersion.objects.all()
    serializer_class = EpisodeVersionSerializer
