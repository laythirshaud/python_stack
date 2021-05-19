from django.urls import path     
from . import views
urlpatterns = [
    path('', views.check),
    path('result', views.result),
    path('delete', views.delete),

]