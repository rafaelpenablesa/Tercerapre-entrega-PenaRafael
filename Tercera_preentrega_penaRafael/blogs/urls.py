from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_blogs, name='lista_blogs'),  
    path('<int:blog_id>/', views.detalle_blog, name='detalle_blog'),  
    path('crear/', views.crear_blog, name='crear_blog'),  
    path('editar/<int:blog_id>/', views.editar_blog, name='editar_blog'),  
    path('eliminar/<int:blog_id>/', views.eliminar_blog, name='eliminar_blog'),  
]