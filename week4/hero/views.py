from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Hero

def HeroMain(request):
    return render(request, 'hero/hero_home.html')

def ShowHero(request, name):
    hero = Hero(name="Black Widow", url_name="black_widow")
    hero.save()
    try:
        hero = Hero.objects.filter(url_name=name)[0]
    except IndexError:
        return HttpResponse("No hero found with identifier " + name)

    context = {
        'hero': hero, 
    }

    return render(request, 'templates/hero_view.html')