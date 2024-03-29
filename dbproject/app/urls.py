from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"), #home url
    path('Organizers/',views.organizers, name= "organizers"), #organizer url
    path('Search/', views.search, name= "search" ), #search url
    path('ChangeView/', views.changeview, name= "changeview"), #changeview url
    path('pflowers/', views.pflowers, name= "pflowers") #popular flowers url
]