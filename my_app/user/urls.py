from django.urls import path, include

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.home, name='home'),
    path('register_view/', views.register_view, name='register_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view')
]