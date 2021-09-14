from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Hero

def HeroMain(request):
    heroes = []

    for hero in Hero.objects.all():
        heroes.append(hero)

    context = {
        'heroes': heroes,
    }

    return render(request, 'hero/hero_home.html', context)

def ShowHero(request, name):
    try:
        hero = Hero.objects.filter(url_name=name)[0]
    except IndexError:
        return HttpResponse("No hero found with identifier " + name)

    context = {
        'hero': hero, 
    }

    return render(request, 'hero/hero_view.html', context)