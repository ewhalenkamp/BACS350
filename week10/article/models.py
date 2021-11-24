from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, models.CASCADE)
    content = models.TextField()

    def get_absolute_url(self):
        return "/article/%s" % self.pk
