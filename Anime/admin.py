from django.forms.models import BaseInlineFormSet
from django.contrib import admin
from .models import Anime
from .models import Genre
from .models import SeasonGenre
from .models import SeasonDescription
from .models import Season
from .models import SeasonAlternativeTitle
from .models import Language
from .models import Episode
from .models import EpisodeSubtitle

# Register your models here.
admin.site.register(Language)
# admin.site.register(Anime)
admin.site.register(Genre)
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
    max_num = 5
    # Seasons should have at least 1 Episode available
    formset = RequiredInlineFormSet


class SeasonGenreInline(admin.StackedInline):
    model = SeasonGenre
    extra = 0
    max_num = 5
    # Animes should have at least 1 Genre avaiable
    formset = RequiredInlineFormSet

class AnimeDescriptionInline(admin.StackedInline):
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
        SeasonAlternativeTitleInline,
        AnimeDescriptionInline,
        SeasonGenreInline,
        EpisodeInline,
    ]


"""
#
# Episode creation admin related view
#
"""


class EpisodeSubtitleInline(admin.StackedInline):
    model = EpisodeSubtitle
    extra = 0
    max_num = 3
    # Episodes should have at least 1 version available
    formset = RequiredInlineFormSet


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    readonly_fields=('episode_code',)
    inlines = [EpisodeSubtitleInline]
