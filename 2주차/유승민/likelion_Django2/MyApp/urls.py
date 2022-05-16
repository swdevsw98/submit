from django.urls import path
from MyApp import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('about/', v.about, name='about'),
    path('about/me', v.me, name='me'),
    path('about/you', v.you, name='you')
]