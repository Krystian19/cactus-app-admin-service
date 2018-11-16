from django.contrib import admin
from .models import Anime, Genre, AnimeGenre, AnimeDescription, Season, SeasonAlternativeTitle, Language

# Register your models here.
admin.site.register(Language)
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeGenre)
admin.site.register(AnimeDescription)
admin.site.register(Season)
admin.site.register(SeasonAlternativeTitle)
