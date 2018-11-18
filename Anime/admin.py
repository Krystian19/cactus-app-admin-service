from django.contrib import admin
from .models import Anime
from .models import Genre
from .models import AnimeGenre
from .models import AnimeDescription
from .models import Season
from .models import SeasonAlternativeTitle 
from .models import Language
from .models import Episode
from .models import EpisodeTitle
from .models import EpisodeVersion

# Register your models here.
admin.site.register(Language)
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeGenre)
admin.site.register(AnimeDescription)
admin.site.register(Season)
admin.site.register(SeasonAlternativeTitle)
admin.site.register(Episode)
admin.site.register(EpisodeTitle)
admin.site.register(EpisodeVersion)
