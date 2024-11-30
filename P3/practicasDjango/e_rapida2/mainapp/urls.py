from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='index'),
    path('about/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('sesión/', views.sesion, name='login'),
    path('registro/', views.registro, name='registro'),
]

handler404 = 'mainapp.views.error404_2'