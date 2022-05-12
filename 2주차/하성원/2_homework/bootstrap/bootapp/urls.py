from django.urls import path
import bootapp.views as ba

urlpatterns = [
    path('', ba.about , name = 'about'),
    path('me/' , ba.me, name = 'me'),
    path('you/', ba.you, name = 'you')
]