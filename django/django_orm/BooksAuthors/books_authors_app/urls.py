from django.urls import path     
from . import views
urlpatterns = [ 
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:id>' , views.showBook),
    path('addAuthorToBook/<int:book_id>', views.addAuthorToBook),
    path('authors',views.index2),
    path('addAuthor',views.addAuthor),
    path('Authors/<int:id>', views.showauthor),
    path('authors/book_to_author/<int:author_id>', views.add_book_to_author),
]