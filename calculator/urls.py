# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the homepage
    path('calculator/', views.calculator, name='calculator'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('calculator11/',views.calculator11,name='calculator11'),
    path('equation_generator/', views.equation_generator, name='equation_generator'),
    path('proof_of_coordinate/',views.proof_of_coordinate,name='proof_of_coordinate'),
    
]
