from django.forms.models import BaseInlineFormSet
from django.contrib import admin
from .models import Anime
from .models import GenreTitleVersion
from .models import Genre
from .models import MovieAlternativeTitle
from .models import MovieSubtitle
from .models import MovieGenre
from .models import MovieDescription
from .models import Movie
from .models import SeasonAlternativeTitle
from .models import SeasonGenre
from .models import SeasonDescription
from .models import Season
from .models import Language
from .models import Episode
from .models import EpisodeSubtitle

# Register your models here.
admin.site.register(Language)
# admin.site.register(Anime)
admin.site.register(GenreTitleVersion)
# admin.site.register(Genre)
admin.site.register(SeasonGenre)
admin.site.register(SeasonDescription)
# admin.site.register(Season)
admin.site.register(SeasonAlternativeTitle)
# admin.site.register(Episode)
admin.site.register(EpisodeSubtitle)


class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form

"""
#
# Genre creation admin related view
#
"""

class GenreTitleVersionInline(admin.StackedInline):
    model = GenreTitleVersion
    extra = 0


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = [GenreTitleVersionInline]

"""
#
# Anime creation admin related view
#
"""


class SeasonInline(admin.StackedInline):
    model = Season
    extra = 0
    max_num = 2
    # Animes should have at least 1 Season avaiable
    formset = RequiredInlineFormSet


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = [SeasonInline]


"""
#
# Season creation admin related view
#
"""


class EpisodeInline(admin.StackedInline):
    model = Episode
    extra = 0
    # max_num = 5
    # # Seasons should have at least 1 Episode available
    # formset = RequiredInlineFormSet


class SeasonGenreInline(admin.StackedInline):
    model = SeasonGenre
    extra = 0
    max_num = 5
    # Animes should have at least 1 Genre avaiable
    formset = RequiredInlineFormSet

class SeasonDescriptionInline(admin.StackedInline):
    model = SeasonDescription
    extra = 0
    max_num = 2
    # Animes should have at least 1 description avaiable, regardless of the language
    formset = RequiredInlineFormSet


class SeasonAlternativeTitleInline(admin.StackedInline):
    model = SeasonAlternativeTitle
    extra = 0
    max_num = 4
    # Seasons may not have alternative titles (not required)
    # formset = RequiredInlineFormSet


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [
        SeasonDescriptionInline,
        SeasonGenreInline,
        EpisodeInline,
        SeasonAlternativeTitleInline,
    ]


"""
#
# Episode creation admin related view
#
"""


class EpisodeSubtitleInline(admin.StackedInline):
    model = EpisodeSubtitle
    extra = 0
    # max_num = 3
    # Episodes should have at least 1 version available
    # formset = RequiredInlineFormSet


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    readonly_fields=('episode_code',)
    inlines = [EpisodeSubtitleInline]


"""
#
# Movie creation admin related view
#
"""

class MovieSubtitleInline(admin.StackedInline):
    model = MovieSubtitle
    extra = 0
    # max_num = 3
    # Episodes should have at least 1 version available
    # formset = RequiredInlineFormSet

class MovieGenreInline(admin.StackedInline):
    model = MovieGenre
    extra = 0
    max_num = 5
    # Animes should have at least 1 Genre avaiable
    formset = RequiredInlineFormSet

class MovieDescriptionInline(admin.StackedInline):
    model = MovieDescription
    extra = 0
    max_num = 2
    # Animes should have at least 1 description avaiable, regardless of the language
    formset = RequiredInlineFormSet


class MovieAlternativeTitleInline(admin.StackedInline):
    model = MovieAlternativeTitle
    extra = 0
    max_num = 4
    # Movies may not have alternative titles (not required)
    # formset = RequiredInlineFormSet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields=('movie_code',)
    inlines = [
        MovieDescriptionInline,
        MovieGenreInline,
        MovieSubtitleInline,
        MovieAlternativeTitleInline,
    ]

