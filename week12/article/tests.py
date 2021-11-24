from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User

class TestSuperHero(TestCase):
    def setUp(self):
        Article.objects.create(title="Captain America Crazy", author=User.objects.all()[0], content="He's kind of a butthole.")