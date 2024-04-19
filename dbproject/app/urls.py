from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"), #home url
    path('Organizers/',views.organizers, name= "organizers"), #organizer url
    path('User/', views.user, name= "user" ), #user url
    path('User/entries/<int:entry>/', views.entries, name= "entries" ), #userentries
    path('User/entries/<int:entry>/form/<str:what>/<str:page>', views.user_forms, name='aform'),
    path('<str:page>/form/<str:what>/<int:entry>', views.user_forms, name='userforms'),
    path('Competitions/', views.competitions, name= "competitions"), #competition url
    path('Competitions/randcomp/', views.randcomp, name = "randcomp"),
    path('pflowers/', views.pflowers, name= "pflowers"), #popular flowers url
    path('<str:obj_type>/delete/<int:obj_id>/', views.delete_object, name='delete_object'), #delete object url

]   