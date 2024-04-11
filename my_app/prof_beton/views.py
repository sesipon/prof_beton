from django.shortcuts import render
from .models import Beton


# Create your views here.

# Create your views here.

def home(request):
    return render(request, 'prof_beton/home.html')

def beton(request):
    beton = Beton.objects.all()
    return render(request, 'prof_beton/beton.html', context={'beton':beton})

