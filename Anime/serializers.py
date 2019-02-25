from .models import Language
from .models import Episode
from rest_framework import serializers

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Language
    fields = ('id', 'name', 'iso_code', 'created_at', 'updated_at')

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Episode
    fields = ('id', 'episodeOrder', 'thumbnail', 'created_at', 'updated_at')
