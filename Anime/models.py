from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=250)
    iso_code = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Languages'

    def __str__(self):
        return self.name + " " + iso_code


class Anime(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Animes'

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Genres'

    def __str__(self):
        return self.title

class AnimeGenre(models.Model):
    """
    This is how Anime and Genres are related ...
    """
    anime_id = models.ForeignKey(
        Anime, on_delete=models.CASCADE, db_column='anime_id')
    genre_id = models.ForeignKey(
        Genre, on_delete=models.CASCADE, db_column='genre_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AnimeGenres'

    def __str__(self):
        return " anime_id: " + str(self.anime_id) + " ,genre_id: " + str(self.genre_id)

class AnimeDescription(models.Model):
    """
    Animes have multiple descriptions depending of the language is available
    """
    anime_id = models.ForeignKey(
        Anime, on_delete=models.CASCADE, db_column='anime_id')
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE, db_column='language_id')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AnimeDescriptions'

    def __str__(self):
        return self.name + " " + iso_code

class Season(models.Model):
    """
    Anime series tend to have multiple seasons
    """
    anime_id = models.ForeignKey(
        Anime, on_delete=models.CASCADE, db_column='anime_id')
    seasonOrder = models.IntegerField()
    title = models.CharField(max_length=250)
    startedAiring = models.DateTimeField()
    stoppedAiring = models.DateTimeField()
    poster = models.CharField(max_length=250)
    background = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Seasons'

    def __str__(self):
        return self.name + " " + iso_code
