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
    path("secretario/info", views.editar_secretario, name="secretario_info"),


    path("analistarh/info/salvar", views.analistarh_salvar, name="analistarh_salvar"),
    path("professor/info/salvar", views.professor_salvar, name="professor_salvar"),
    path("secretario/info/salvar", views.secretario_salvar, name="secretario_salvar"),

    path("analistarh/info/apagar", views.analistarh_apagar, name="analistarh_apagar"),
    path("professor/info/apagar", views.professor_apagar, name="professor_apagar"),
    path("secretario/info/apagar", views.secretario_apagar, name="secretario_apagar"),
]
