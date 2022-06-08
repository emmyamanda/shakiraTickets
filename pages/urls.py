from django.urls import path

from . import views

urlpatterns = [
    path('gigs', views.index, name='index'),
    path('about-us', views.aboutUs, name='about-us'),
    path('live-show/<str:liveShow>', views.liveShow, name='live-show'),
]