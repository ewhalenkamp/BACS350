from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def ArticleMain(request):
    articles = []

    for article in Article.objects.all():
        articles.append(article)

    context = {
        'articles': articles,
    }

    return render(request, 'article/article_home.html', context)

def ShowArticle(request, pk):
    try:
        article = Article.objects.filter(pk=pk)[0]
    except IndexError:
        return HttpResponse("No hero found with identifier " + pk)

    context = {
        'article': article, 
    }

    return render(request, 'article/article_view.html', context)

class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_home')