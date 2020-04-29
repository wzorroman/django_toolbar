from django.urls import path

from . import views
from almacen import views as view_almacen

urlpatterns = [
    path('', view_almacen.index, name='index'),
    path('prueba/', view_almacen.EjemploView.as_view()),
    
]