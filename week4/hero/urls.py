from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HeroMain),
    path('<int:pk>', ShowHero, name='hero_view'),
]