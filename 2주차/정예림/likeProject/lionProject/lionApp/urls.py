from django.urls import path
from lionApp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('about/me', views.me, name = 'me'),
    path('about/you', views.you, name = 'you'),
]