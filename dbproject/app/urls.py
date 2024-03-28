from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('Organizers/',views.organizers, name= "organizers"),
    path('Search/', views.search, name= "search" ),
    path('ChangeView/', views.changeview, name= "changeview"),
    path('pflowers/', views.pflowers, name= "pflowers")
]