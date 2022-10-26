from django.urls import path
from . import views

urlpattern = [

  path('', views.index, name='index'),
  path('sobre/', views.sobre, name='sobre'),
]