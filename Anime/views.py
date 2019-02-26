from django.shortcuts import render
from rest_framework import viewsets
from Anime.serializers import LanguageSerializer
from Anime.serializers import AnimeSerializer
from Anime.serializers import GenreSerializer
from Anime.serializers import SeasonSerializer
from Anime.serializers import EpisodeSerializer
from .models import Language
from .models import Anime
from .models import Episode
from .models import Genre
from .models import Season

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

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

