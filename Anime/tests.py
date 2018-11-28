from django.test import TestCase
from .models import Anime

# Anime model related tests
class AnimeTestCase(TestCase):
  GENEREIC_ANIME_TITLE = 'Generic Anime Name'
  def setUp(self):
    Anime.objects.create(
      title=self.GENEREIC_ANIME_TITLE,
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
    if test_anime.title != self.GENEREIC_ANIME_TITLE:
      self.fail('Last Anime record doest not have the expected title value')

    # Does the Anime model have a created_at field ?
    if test_anime.created_at is None:
      self.fail('The Anime model does not have a created_at field')

    # Does the Anime model have a updated_at field ?
    if test_anime.updated_at is None:
      self.fail('The Anime model does not have a updated_at field')