from django.db import models

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

# This is how Anime and Genres are related ...
class AnimeGenre(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE, db_column='anime_id')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='genre_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AnimeGenres'

    def __str__(self):
        return " anime_id: " + str(self.anime_id) + " ,genre_id: " + str(self.genre_id)