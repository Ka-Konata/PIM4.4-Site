from django.urls import path
from . import views

app_name = "professor"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("conteudo", views.procurar_conteudo, name="conteudo"),
    path("conteudo/info", views.editar_conteudo, name="conteudo_info"),
    path("disciplinas", views.acessar_disciplinas, name="disciplinas"),
    path("disciplinas/alunos", views.acessar_alunos_em_disciplinas, name="alunos_em_disciplinas"),
    path("mapa_de_notas", views.mapa_de_notas, name="mapa_de_notas")
]
