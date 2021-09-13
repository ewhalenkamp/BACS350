from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Hero

def HeroMain(request):
    return render(request, 'hero/index.html')

def ShowHero(request, pk):
    try:
        hero = Hero.objects.filter(pk=pk)[0]
    except IndexError:
        return HttpResponse("No hero found with id " + str(pk))

    context = {
        'hero': hero, 
    }

    return render(request, 'templates/hero_view.html')