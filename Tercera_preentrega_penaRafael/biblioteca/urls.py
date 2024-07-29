from django.urls import path
from . import views

urlpatterns = [
    path('donar_libro/', views.donar_libro, name='donar_libro'),
    path('seleccionar_libro_prestamo/', views.seleccionar_libro_prestamo, name='seleccionar_libro_prestamo'),
    path('seleccionar_libro_devolucion/', views.seleccionar_libro_devolucion, name='seleccionar_libro_devolucion'),
    path('pedir_prestamo/<int:libro_id>/', views.pedir_prestamo, name='pedir_prestamo'),
    path('registrar_devolucion/<int:libro_id>/', views.registrar_devolucion, name='registrar_devolucion'),
    path('buscar/', views.buscar, name='buscar'),
]
