from django.test import TestCase
from .models import Anime
from .models import Language
from .models import Genre

# Anime model related tests
class AnimeTestCase(TestCase):
  GENERIC_ANIME_TITLE = 'Generic Anime Name'

  def setUp(self):
    Anime.objects.create(
      title=self.GENERIC_ANIME_TITLE,
    )

  def test_anime_model_integrity(self):
    """
    Current Anime model does not to the declared integrity.
    """

    test_anime = Anime.objects.last()

    # Was the anime created successfully ?
    if test_anime is None:
      self.fail('Anime registry was not created properly')

    # Does the last Anime record have the expected title
    if test_anime.title != self.GENERIC_ANIME_TITLE:
      self.fail('Last Anime record doest not have the expected title value')

    # Does the Anime model have a created_at field ?
    if test_anime.created_at is None:
      self.fail('The Anime model does not have a created_at field')

    # Does the Anime model have a updated_at field ?
    if test_anime.updated_at is None:
      self.fail('The Anime model does not have a updated_at field')

# Language model related tests
class LanguageTestCase(TestCase):
  GENERIC_LANGUAGE_NAME = 'Generic Language Name'
  GENERIC_LANGUAGE_ISO_CODE = 'es'

  def setUp(self):
    Language.objects.create(
      name=self.GENERIC_LANGUAGE_NAME,
      iso_code=self.GENERIC_LANGUAGE_ISO_CODE
    )

  def test_language_model_integrity(self):
    """
    Current Language model does not to the declared integrity.
    """
    test_language = Language.objects.last()

    # Was the Language created successfully ?
    if test_language is None:
      self.fail('Language registry was not created properly')

    # Does the last Language record have the expected name ?
    if test_language.name != self.GENERIC_LANGUAGE_NAME:
      self.fail('Last Language record doest not have the expected name value')

    # Does the last Language record have the expected iso_code ?
    if test_language.iso_code != self.GENERIC_LANGUAGE_ISO_CODE:
      self.fail('Last Language record doest not have the expected iso_code value')

    # Does the Language model have a created_at field ?
    if test_language.created_at is None:
      self.fail('The Language model does not have a created_at field')

    # Does the Language model have a updated_at field ?
    if test_language.updated_at is None:
      self.fail('The Language model does not have a updated_at field')

# Genre model related tests
class GenreTestCase(TestCase):
  GENERIC_GENRE_TITLE = 'Generic Genre Title'
  GENERIC_GENRE_THUMBNAIL = 'thumbnail.jpg'

  def setUp(self):
    Genre.objects.create(
      title=self.GENERIC_GENRE_TITLE,
      thumbnail=self.GENERIC_GENRE_THUMBNAIL,
    )

  def test_genre_model_integrity(self):
    """
    Current Genre model does not to the declared integrity.
    """
    test_genre = Genre.objects.last()

    # Was the Genre created successfully ?
    if test_genre is None:
      self.fail('Genre registry was not created properly')

    # Does the last Genre record have the expected name ?
    if test_genre.title != self.GENERIC_GENRE_TITLE:
      self.fail('Last Genre record doest not have the expected title value')

    # Does the last Genre record have the expected iso_code ?
    if test_genre.thumbnail != self.GENERIC_GENRE_THUMBNAIL:
      self.fail('Last Genre record doest not have the expected thumbnail value')

    # Does the Genre model have a created_at field ?
    if test_genre.created_at is None:
      self.fail('The Genre model does not have a created_at field')

    # Does the Genre model have a updated_at field ?
    if test_genre.updated_at is None:
      self.fail('The Genre model does not have a updated_at field')