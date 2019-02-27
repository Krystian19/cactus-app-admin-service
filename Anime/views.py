from django.shortcuts import render
from rest_framework import viewsets
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

