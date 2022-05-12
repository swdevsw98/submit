from django.contrib import admin
from django.urls import path
from TossApp import views as ts

urlpatterns = [
    path('', ts.about, name='about'),
    path('me/', ts.aboutMe, name='aboutMe'),
    path('you/', ts.aboutYou, name='aboutYou')
]