from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Hero
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

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

class HeroDetailView(DetailView):
    model = Hero

class HeroCreateView(CreateView):
    model = Hero
    fields = ['name', 'identity']
    template_name_suffix = '_create_form'

    def post(self, request, *args, **kwargs):
        self.object.url_name = self.object.name.lower().replace(" ", "_")
        return super().post(request, *args, **kwargs)

class HeroUpdateView(UpdateView):
    model = Hero
    fields = ['name', 'identity']
    template_name_suffix = '_update_form'

    def post(self, request, *args, **kwargs):
        self.object.url_name = self.object.name.lower().replace(" ", "_")
        return super().post(request, *args, **kwargs)

class HeroDeleteView(DeleteView):
    model = Hero
    success_url = reverse_lazy('hero_home')