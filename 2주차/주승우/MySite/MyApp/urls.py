from django.urls import path
import MyApp.views as views

urlpatterns = [
    path('', views.about, name='about'),
    path('me/', views.me, name='about_me'),
    path('you/', views.you, name='about_you'),
]