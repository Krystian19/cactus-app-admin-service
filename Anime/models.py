import uuid
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
    thumbnail = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Genres"

    def __str__(self):
        return self.title

class GenreLanguageVersion(models.Model):
    """
    Genres can have different titles throughout different languages
    """

    title = models.CharField(max_length=250)
    genre_id = models.ForeignKey(
        Genre, on_delete=models.CASCADE, db_column="genre_id"
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "GenreLanguageVersion"

    def __str__(self):
        return "GenreLanguageVersion Episode " + self.genre_id + ", Language: " + self.language_id


# TODO Work in the Movie model, and Movie Subtitle.

class Season(models.Model):
    """
    Anime series tend to have multiple seasons
    """

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column="anime_id")
    seasonOrder = models.IntegerField()
    title = models.CharField(max_length=250)
    startedAiring = models.DateTimeField()
    stoppedAiring = models.DateTimeField(blank=True, null=True)
    poster = models.CharField(max_length=250, blank=True, null=True)
    background = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Seasons"

    def __str__(self):
        return str(self.anime_id) + " ,Season: " + str(self.seasonOrder)


class SeasonGenre(models.Model):
    """
    This is how Anime and Genres are related ...
    """

    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, db_column="season_id"
    )
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column="genre_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "SeasonGenres"

    def __str__(self):
        return " season_id: " + str(self.season_id) + " ,genre_id: " + str(self.genre_id)


class SeasonDescription(models.Model):
    """
    Seasons have multiple descriptions based off the language they are in.
    """

    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, db_column="season_id"
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "SeasonDescriptions"

    def __str__(self):
        return (
            "Season id: " + str(self.season_id) + " ,Language: " + str(self.language_id)
        )


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
    thumbnail = models.CharField(max_length=250, blank=True, null=True)
    season_id = models.ForeignKey(
        Season, on_delete=models.CASCADE, db_column="season_id"
    )
    episode_code = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Episodes"

    def __str__(self):
        return str(self.season_id) + " , Episode #: " + str(self.episodeOrder)


class EpisodeSubtitle(models.Model):
    """
     Episodes are available in multiple languages.
    """

    subtitle_code = models.UUIDField(default=uuid.uuid4, editable=False)
    episode_id = models.ForeignKey(
        Episode, on_delete=models.CASCADE, db_column="episode_id"
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "EpisodeSubtitles"

    def __str__(self):
        return "Subtitle for episode: " + str(self.episode_id) + " , Language: " + str(self.language_id)
