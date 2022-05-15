from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def me(request):
    return render(request, 'me.html')


def you(request):
    return render(request, 'you.html')