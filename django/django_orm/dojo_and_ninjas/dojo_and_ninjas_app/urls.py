from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show', views.srap),
    path('show2', views.secand)
]