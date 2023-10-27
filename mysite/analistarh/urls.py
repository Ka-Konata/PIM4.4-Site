from django.urls import path
from . import views

app_name = "analistarh"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("analistarh", views.procurar_analista, name="analistarh"),
    path("analistarh/info", views.editar_analista, name="analistarh_info"),
    path("professor", views.procurar_professor, name="professor"),
    path("professor/info", views.editar_professor, name="professor_info"),
    path("secretario", views.procurar_secretario, name="secretario"),
    path("secretario/info", views.editar_secretario, name="secretario_info")
]
