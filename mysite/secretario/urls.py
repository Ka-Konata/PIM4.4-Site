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
    path("aluno_em_curso/info", views.editar_aluno_em_curso, name="aluno_em_curso_info"),
    path("aluno/info", views.editar_aluno, name="editar_aluno"),
    path("curso/info", views.editar_curso, name="editar_curso"),
    path("turma/info", views.editar_turma, name="editar_turma"),
    path("disciplina/info", views.editar_disciplina, name="editar_disciplina"),


    path("professor_em_turma/info/salvar", views.professor_em_turma_salvar, name="professor_em_turma_salvar"),
    path("disciplina_em_curso/info/salvar", views.disciplina_em_curso_salvar, name="disciplina_em_curso_salvar"),
    path("aluno_em_curso/info/salvar", views.aluno_em_curso_salvar, name="aluno_em_curso_salvar"),
    path("aluno/info/salvar", views.aluno_salvar, name="aluno_salvar"),
    path("curso/info/salvar", views.curso_salvar, name="curso_salvar"),
    path("turma/info/salvar", views.turma_salvar, name="turma_salvar"),
    path("disciplina/info/salvar", views.disciplina_salvar, name="disciplina_salvar"),


    path("professor_em_turma/info/apagar", views.professor_em_turma_apagar, name="professor_em_turma_apagar"),
    path("disciplina_em_curso/info/apagar", views.disciplina_em_curso_apagar, name="disciplina_em_curso_apagar"),
    path("aluno_em_curso/info/apagar", views.aluno_em_curso_apagar, name="aluno_em_curso_apagar"),
    path("aluno/info/apagar", views.aluno_apagar, name="aluno_apagar"),
    path("curso/info/apagar", views.curso_apagar, name="curso_apagar"),
    path("turma/info/apagar", views.turma_apagar, name="turma_apagar"),
    path("disciplina/info/apagar", views.disciplina_apagar, name="disciplina_apagar")
]
