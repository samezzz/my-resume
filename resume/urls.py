from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skills&projects/', views.skills_projects, name='skills-projects'),
    path('contact/', views.contact, name='contact'),
]
