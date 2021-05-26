from django.urls import path
from . import views
urlpatterns = [
    path('', views.inde),
    path('shows/', views.index),
    path('shows/new/', views.new),
    path('create', views.create),
    path('shows/<int:id>', views.index3),
    path('shows/<int:id>/edit', views.index4),
    path('shows/editthis', views.edit),
    path('delete/<int:id>/', views.delete),
]