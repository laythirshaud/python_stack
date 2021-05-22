from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('find', views.index2),
    path('updat', views.updat),
]