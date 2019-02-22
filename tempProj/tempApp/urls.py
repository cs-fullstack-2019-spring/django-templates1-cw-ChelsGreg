from django.urls import path
from .import views

# DIRECTING ROUTES
urlpatterns = [
    path('home/base/', views.toBase, name='base'),
    path('home/about/', views.toAbout, name='about'),
    path('home/', views.index, name='index'),

    ]