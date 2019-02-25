from django.shortcuts import render
from rest_framework import viewsets
from Anime.serializers import LanguageSerializer
from Anime.serializers import EpisodeSerializer
from .models import Language
from .models import Episode

# Create your views here.
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

