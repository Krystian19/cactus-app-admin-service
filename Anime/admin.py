from django.forms.models import BaseInlineFormSet
from django.contrib import admin
from .models import Anime
from .models import GenreTitleVersion
from .models import Genre
from .models import ReleaseType
from .models import ReleaseAlternativeTitle
from .models import ReleaseGenre
from .models import ReleaseDescription
from .models import Release
from .models import Language
from .models import Episode
from .models import EpisodeSubtitle

# Register your models here.
admin.site.register(Language)
# admin.site.register(Anime)
admin.site.register(GenreTitleVersion)
# admin.site.register(Genre)
admin.site.register(ReleaseType)
admin.site.register(ReleaseGenre)
admin.site.register(ReleaseDescription)
# admin.site.register(Release)
admin.site.register(ReleaseAlternativeTitle)
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


class ReleaseInline(admin.StackedInline):
    model = Release
    extra = 0
    max_num = 2
    # Animes should have at least 1 Release avaiable
    formset = RequiredInlineFormSet


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = [ReleaseInline]


"""
#
# Release creation admin related view
#
"""


class EpisodeInline(admin.StackedInline):
    model = Episode
    extra = 0
    # max_num = 5
    # # Releases should have at least 1 Episode available
    # formset = RequiredInlineFormSet


class ReleaseGenreInline(admin.StackedInline):
    model = ReleaseGenre
    extra = 0
    max_num = 5
    # Animes should have at least 1 Genre avaiable
    formset = RequiredInlineFormSet

class ReleaseDescriptionInline(admin.StackedInline):
    model = ReleaseDescription
    extra = 0
    max_num = 2
    # Animes should have at least 1 description avaiable, regardless of the language
    formset = RequiredInlineFormSet


class ReleaseAlternativeTitleInline(admin.StackedInline):
    model = ReleaseAlternativeTitle
    extra = 0
    max_num = 4
    # Releases may not have alternative titles (not required)
    # formset = RequiredInlineFormSet


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        ReleaseDescriptionInline,
        ReleaseGenreInline,
        EpisodeInline,
        ReleaseAlternativeTitleInline,
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
