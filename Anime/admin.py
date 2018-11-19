from django.forms.models import BaseInlineFormSet
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
# admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(AnimeGenre)
admin.site.register(AnimeDescription)
# admin.site.register(Season)
admin.site.register(SeasonAlternativeTitle)
# admin.site.register(Episode)
admin.site.register(EpisodeTitle)
admin.site.register(EpisodeVersion)

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
class AnimeGenreInline(admin.StackedInline):
    model = AnimeGenre
    extra = 1
    max_num = 5
    formset = RequiredInlineFormSet


class SeasonInline(admin.StackedInline):
    model = Season
    extra = 1
    max_num = 2
    formset = RequiredInlineFormSet


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = [AnimeGenreInline, SeasonInline]

"""
#
# Season creation admin related view
#
"""
class SeasonAlternativeTitleInline(admin.StackedInline):
    model = SeasonAlternativeTitle
    extra = 1
    max_num = 1
    # Seasons may not have alternative titles (not required)
    # formset = RequiredInlineFormSet

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [SeasonAlternativeTitleInline]

"""
#
# Episode creation admin related view
#
"""
class EpisodeTitleInline(admin.StackedInline):
    model = EpisodeTitle
    extra = 1
    max_num = 3
    # Episodes should have at least 1 title available
    formset = RequiredInlineFormSet

class EpisodeVersionInline(admin.StackedInline):
    model = EpisodeVersion
    extra = 1
    max_num = 3
    # Episodes should have at least 1 version available
    formset = RequiredInlineFormSet

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    inlines = [EpisodeTitleInline, EpisodeVersionInline]
