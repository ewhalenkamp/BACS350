from django.shortcuts import render

def ShowHero(request, hero):
    template = 'hero/' + str(hero) + '.html'
    return render(request, template)