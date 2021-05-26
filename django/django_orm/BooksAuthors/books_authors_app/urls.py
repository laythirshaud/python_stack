from django.urls import path     
from . import views
urlpatterns = [ 
    path('', views.index),  
    path('show', views.show),
    path('view/<int:id>', views.view),
    path('add', views.add),
]