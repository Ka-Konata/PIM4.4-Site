from django.urls import path
from . import views

app_name = "secretario"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("aluno", views.procurar_aluno, name="aluno"),
    path("curso", views.procurar_curso, name="curso"),
    path("turma", views.procurar_turma, name="turma"),
    path("disciplina", views.procurar_disciplina, name="disciplina"),
    path("aluno/info", views.editar_aluno, name="aluno_info"),
    path("curso/info", views.editar_curso, name="curso_info"),
    path("turma/info", views.editar_turma, name="turma_info"),
    path("disciplina/info", views.editar_disciplina, name="disciplina_info"),

    path("professor_em_turma", views.procurar_professor_em_turma, name="professor_em_turma"),
    path("disciplina_em_curso", views.procurar_disciplina_em_curso, name="disciplina_em_curso"),
    path("aluno_em_curso", views.procurar_aluno_em_curso, name="aluno_em_curso"),
    
    path("professor_em_turma/info", views.editar_professor_em_turma, name="professor_em_turma_info"),
    path("disciplina_em_curso/info", views.editar_disciplina_em_curso, name="disciplina_em_curso_info"),
    path("aluno_em_curso/info", views.editar_aluno_em_curso, name="aluno_em_curso_info")
]
