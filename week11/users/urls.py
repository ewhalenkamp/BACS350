from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import register, Logout

urlpatterns = [
    path('register', register, name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page="/hero/"), name="logout"),
]