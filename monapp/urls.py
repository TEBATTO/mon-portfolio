from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Vue d'accueil (modifiez selon vos besoins)
    path('interests/', views.interests, name='interests'),
    path('skills/', views.skills, name='skills'),
    path('about-me/', views.about_me, name='about_me'),
    path('courses/', views.courses, name='courses'),
    path('mes-projects/', views.mes_projects, name='mes_projects'),
]
