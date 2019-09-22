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
        return str(self.name) + " " + str(self.iso_code)


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

class GenreTitleVersion(models.Model):
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
        db_table = "GenreTitleVersion"

    def __str__(self):
        return "GenreTitleVersion Genre " + str(self.genre_id) + ", Language: " + str(self.language_id)


class ReleaseType(models.Model):
    """
    Anime Releases can be Seasons, Movies, OVAs, Specials ...
    """

    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ReleaseTypes"

    def __str__(self):
        return " Release Type: " + str(self.title)

class Release(models.Model):
    """
    Anime series tend to have multiple releases
    """

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column="anime_id")
    release_type_id = models.ForeignKey(
        ReleaseType, on_delete=models.CASCADE, db_column="release_type_id"
    )

    release_order = models.IntegerField()
    title = models.CharField(max_length=250, blank=True, null=True)
    startedAiring = models.DateTimeField()
    stoppedAiring = models.DateTimeField(blank=True, null=True)
    poster = models.CharField(max_length=250, blank=True, null=True)
    background = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Releases"

    def __str__(self):
        return str(self.anime_id) + " ,Release: " + str(self.release_order)


class ReleaseGenre(models.Model):
    """
    This is how Releases and Genres are related ...
    """

    release_id = models.ForeignKey(
        Release, on_delete=models.CASCADE, db_column="release_id"
    )
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column="genre_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ReleaseGenres"

    def __str__(self):
        return " release_id: " + str(self.release_id) + " ,genre_id: " + str(self.genre_id)


class ReleaseDescription(models.Model):
    """
    Releases have multiple descriptions based off the language they are in.
    """

    release_id = models.ForeignKey(
        Release, on_delete=models.CASCADE, db_column="release_id"
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column="language_id"
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ReleaseDescriptions"

    def __str__(self):
        return (
            "Release id: " + str(self.release_id) + " ,Language: " + str(self.language_id)
        )


class ReleaseAlternativeTitle(models.Model):
    """
    Releases usually have more than one title
    """

    release_id = models.ForeignKey(
        Release, on_delete=models.CASCADE, db_column="release_id"
    )
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ReleaseAlternativeTitles"

    def __str__(self):
        return str(self.release_id) + " , Alternative title: " + str(self.title)


class Episode(models.Model):
    episode_order = models.IntegerField()
    thumbnail = models.CharField(max_length=250, blank=True, null=True)
    release_id = models.ForeignKey(
        Release, on_delete=models.CASCADE, db_column="release_id"
    )
    episode_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Episodes"

    def __str__(self):
        return str(self.release_id) + " , Episode #: " + str(self.episode_order)


class EpisodeSubtitle(models.Model):
    """
     Episodes are available in multiple languages.
    """

    subtitle_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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
