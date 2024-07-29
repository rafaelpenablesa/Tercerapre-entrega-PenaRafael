from django.urls import path
from . import views

urlpatterns = [
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('buscar/', views.buscar, name='buscar'),
]
