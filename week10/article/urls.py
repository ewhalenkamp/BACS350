from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ArticleMain, name='article_home'),
    path('create', ArticleCreateView.as_view(template_name="article/article_create_form.html"), name="article_create"),
    path('update/<pk>', ArticleUpdateView.as_view(template_name="article/article_update_form.html"), name="article_update"),
    path('delete/<pk>', ArticleDeleteView.as_view(template_name="article/article_delete_form.html"), name="article_delete"),
    path('<int:pk>', ShowArticle, name='article_view'),

]