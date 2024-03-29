from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"), #home url
    path('Organizers/',views.organizers, name= "organizers"), #organizer url
    path('User/', views.user, name= "user" ), #user url
    path('Competitions/', views.competitions, name= "competitions"), #competition url
    path('pflowers/', views.pflowers, name= "pflowers") #popular flowers url
]