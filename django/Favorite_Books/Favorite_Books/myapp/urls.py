from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('registration',views.registration),
    path('success',views.success),
    path("logout",views.logout),
    path("login",views.login),
    path("books",views.addbooks),
    path("show/<int:id>",views.showbook),
]