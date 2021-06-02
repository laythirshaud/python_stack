from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path("login",views.login),
    path('registration',views.registration),

    path('add_thought',views.add_thought),
    path('thought/<int:id>',views.thought),
    
    path('unlike/<int:id>',views.unlikethought),
    path('like/<int:id>',views.likethought),

    path('success',views.success),
    path("logout",views.logout),
]