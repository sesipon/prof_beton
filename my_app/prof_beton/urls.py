from django.urls import path
from . import views

app_name = 'prof_beton'

urlpatterns = [
    path('', views.home, name='home'),
    path('beton/', views.beton, name='beton'),
]
