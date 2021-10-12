from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HeroMain, name='hero_home'),
    path('create', HeroCreateView.as_view(template_name="hero/hero_create_form.html"), name="hero_create"),
    path('update/<pk>', HeroUpdateView.as_view(template_name="hero/hero_update_form.html"), name="hero_update"),
    path('delete/<pk>', HeroDeleteView.as_view(template_name="hero/hero_delete_form.html"), name="hero_delete"),
    path('<str:name>', ShowHero, name='hero_view'),

]