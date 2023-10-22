from django.urls import path
from . import views

app_name = "analistarh"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("analistarh", views.procurar_analista, name="analistarh"),
    path("professor", views.procurar_analista, name="professor"),
    path("secretario", views.procurar_analista, name="secretario")
]
