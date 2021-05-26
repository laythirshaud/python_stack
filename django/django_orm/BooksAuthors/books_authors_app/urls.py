from django.urls import path     
from . import views
urlpatterns = [ 
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:id>' , views.showBook),
    path('addAuthorToBook/<int:book_id>', views.addAuthorToBook)
]