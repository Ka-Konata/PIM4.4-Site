from django.urls import path
from . import views

app_name = "professor"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("conteudo", views.procurar_conteudo, name="conteudo"),
    path("conteudo/listar", views.acessar_conteudos, name="acessar_conteudos"),
    path("disciplinas", views.acessar_disciplinas, name="disciplinas"),
    path("disciplinas/alunos", views.acessar_alunos_em_disciplinas, name="alunos_em_disciplinas"),
    path("mapa_de_notas", views.mapa_de_notas, name="mapa_de_notas"),

    
    path("conteudo/listar/download", views.download_conteudo, name="download_conteudo"),
    path("conteudo/listar/info", views.editar_conteudo, name="info_conteudo"),
    path("conteudo/listar/info/salvar", views.conteudo_salvar, name="conteudo_salvar"),
    path("conteudo/listar/info/apagar", views.conteudo_apagar, name="conteudo_apagar"),
    path("disciplinas/alunos/info", views.info_alunos_em_disciplinas, name="info_alunos_em_disciplinas"),
    path("disciplinas/alunos/info/salvar", views.alunos_em_disciplinas_salvar, name="disciplina_cursada_salvar")
]
