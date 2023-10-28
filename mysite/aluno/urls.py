from django.urls import path
from . import views

app_name = "aluno"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("curso", views.acessar_cursos, name="acessar_cursos"),
    path("curso/disciplina", views.acessar_disciplinas, name="acessar_disciplinas"),
    path("curso/disciplina/conteudo", views.acessar_conteudos, name="acessar_conteudos"),
    path("curso/disciplina/conteudo/download", views.download_conteudo, name="download_conteudo"),
    path("notas_e_faltas", views.notas_e_faltas, name="notas_e_faltas"),
    
    path("declaracao", views.download_declaracao, name="declaracao"),
    path("historico", views.download_historico, name="historico"),
    path("relatorio", views.download_relatorio, name="relatorio"),
    path("boletim", views.download_boletim, name="boletim")
]
