from django.urls import path

from . import views

urlpatterns = [
    path('gigs', views.index, name='index'),
]