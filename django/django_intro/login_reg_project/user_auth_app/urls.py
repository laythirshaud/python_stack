from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.regester),
    path('welcome', views.welcome),
    path('logout', views.logout)

]
