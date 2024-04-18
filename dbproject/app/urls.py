from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"), #home url
    path('Organizers/',views.organizers, name= "organizers"), #organizer url
    path('User/', views.user, name= "user" ), #user url
    path('User/entries/<int:entry>/', views.entries, name= "entries" ), #userentries
    path('<str:page>/form/<str:what>/', views.user_forms, name='userforms'),
    path('Competitions/', views.competitions, name= "competitions"), #competition url
    path('Competitions/randcomp/', views.randcomp, name = "randcomp"),
    path('pflowers/', views.pflowers, name= "pflowers"), #popular flowers url
    path('<str:obj_type>/delete/<int:obj_id>/', views.delete_object, name='delete_object'), #delete object url
    path('User/update/<int:u_id>/', views.update_user, name='update_user'), #update user url
    path('Organizers/update/<int:o_id>/', views.update_organizer, name='update_organizer'), #update organizer url
    path('Competitions/update/<int:c_id>/', views.update_competition, name='update_competition'), #update compettion url
]