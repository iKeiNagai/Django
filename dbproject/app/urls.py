from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"), #home url
    path('Organizers/',views.organizers, name= "organizers"), #organizer url
    path('User/', views.search, name= "user" ), #user url
    path('Competitions/', views.changeview, name= "competitions"), #competition url
    path('pflowers/', views.pflowers, name= "pflowers") #popular flowers url
]