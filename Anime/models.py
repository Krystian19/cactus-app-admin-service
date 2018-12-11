from django.db import models
from datetime import datetime


class Language(models.Model):
    name = models.CharField(max_length=250)
    iso_code = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Languages"

    def __str__(self):
        return self.name + " " + self.iso_code


class Anime(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Animes"

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250, default="test.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Genres"

    def __str__(self):
        return self.title


class AnimeGenre(models.Model):
    """
    This is how Anime and Genres are related ...
    """

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column="anime_id")
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column="genre_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "AnimeGenres"

    def __str__(self):
        return " anime_id: " + str(self.anime_id) + " ,genre_id: " + str(self.genre_id)


class AnimeDescription(models.Model):
    """
    Animes have multiple descriptions depending of the language is available
    """

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column="anime_id")
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "AnimeDescriptions"

    def __str__(self):
        return str(self.anime_id) + " ,Language: " + str(self.language_id)


class Season(models.Model):
    """
    Anime series tend to have multiple seasons
    """

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column="anime_id")
    seasonOrder = models.IntegerField()
    title = models.CharField(max_length=250)
    startedAiring = models.DateTimeField()
    stoppedAiring = models.DateTimeField(blank=True, null=True)
    poster = models.CharField(max_length=250, default="test.jpg")
    background = models.CharField(max_length=250, default="test.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Seasons"

    def __str__(self):
        return str(self.anime_id) + " ,Season: " + str(self.seasonOrder)


class SeasonAlternativeTitle(models.Model):
    """
    Seasons usually have more than one title
    """

    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, db_column="season_id"
    )
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "SeasonAlternativeTitles"

    def __str__(self):
        return str(self.season_id) + " , Alternative title: " + str(self.title)


class Episode(models.Model):
    episodeOrder = models.IntegerField()
    thumbnail = models.CharField(max_length=250, default="test.jpg")
    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, db_column="season_id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Episodes"

    def __str__(self):
        return str(self.season_id) + " , Episode #: " + str(self.episodeOrder)


class EpisodeVersion(models.Model):
    """
     Episodes are available in multiple languages.
    """

    episode_url = models.TextField(max_length=250)
    episode_id = models.ForeignKey(
        Episode, on_delete=models.CASCADE, db_column="episode_id"
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    title = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "EpisodeVersions"

    def __str__(self):
        return str(self.episode_id) + " , Language: " + str(self.language_id)
