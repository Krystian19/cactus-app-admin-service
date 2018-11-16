from django.contrib import admin
from .models import Anime, Genre, AnimeGenre

# Register your models here.
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeGenre)
