from django.test import TestCase
from .models import Hero

# Create your tests here.
class HeroModelTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name="Superman", identity="Clark Kent", url_name="superman")
        Hero.objects.create(name="Batman", identity="Bruce Wayne", url_name="batman")

    def test_heroes(self):
        superman = Hero.objects.filter(name="Superman")[0]
        batman = Hero.objects.filter(name="Batman")[0]
        self.assertEqual(batman.identity, "Bruce Wayne")
        self.assertEqual(superman.identity, "Clark Kent")