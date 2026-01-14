from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('pdf/', views.generar_pdf, name='generar_pdf'),
]