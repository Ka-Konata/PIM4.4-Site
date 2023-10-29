import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils
from login.views import is_logged, set_cookies

conn = api.Connection(os.environ["API_URL"])

def check_login(request: HttpRequest) -> [dict, api.Login]:
    # Verificando se o usuário está logado.
    logged, login = is_logged(request)
    if not logged:
        return redirect("login:index"), login

    # Fazendo o request na API
    response, secretario = conn.consultar.secretario(login.token, login.id)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Verificando se o refresh_token é válido
        refresh = conn.refresh(login.id, login.token, login.refresh_token)
        if refresh.status_code == 400:
            return redirect("login:index"), login
        
        # Caso o refresh tenha tido êxito
        login = api.Login()
        login.set_values_with_response(refresh)
        # Fazendo o request na API novamente com o novo token
        response, secretario = conn.consultar.secretario(login.token, login.id)

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.SECRETARIO:
        return redirect("erros:403"), login
    
    # Caso tudo ocorra bem
    context["secretario"] = secretario
    return context, login

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do secretario de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/index.html", context), login)

def procurar_aluno(request: HttpRequest):
    """Página inicial para buscas de aluno"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, alunos = conn.procurar.aluno(login.token, filtro)
    context["resultados"] = alunos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_aluno.html", context), login)

def procurar_curso(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, cursos = conn.procurar.curso(login.token, filtro)
    context["resultados"] = cursos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_curso.html", context), login)

def procurar_turma(request: HttpRequest):
    """Página inicial para buscas de turma"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, turmas = conn.procurar.turma(login.token, filtro)
    context["resultados"] = turmas
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_turma.html", context), login)

def procurar_disciplina(request: HttpRequest):
    """Página inicial para buscas de disciplina"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplinas = conn.procurar.disciplina(login.token, filtro)
    context["resultados"] = disciplinas
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_disciplina.html", context), login)

def editar_aluno(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de aluno"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, aluno = conn.consultar.aluno(login.token, id)
        context["cadastro"] = aluno
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_aluno.html", context), login)

def editar_curso(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, curso = conn.consultar.curso(login.token, id)
        context["cadastro"] = curso
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_curso.html", context), login)

def editar_turma(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de turma"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, turma = conn.consultar.turma(login.token, id)
        context["cadastro"] = turma
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_turma.html", context), login)

def editar_disciplina(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de disciplina"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, disciplina = conn.consultar.disciplina(login.token, id)
        context["cadastro"] = disciplina
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_disciplina.html", context), login)

def procurar_professor_em_turma(request: HttpRequest):
    """Página inicial para buscas de disciplina_ministrada"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplina_ministrada = conn.procurar.disciplina_ministrada(login.token, filtro)
    context["resultados"] = disciplina_ministrada
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_professor_em_turma.html", context), login)

def procurar_disciplina_em_curso(request: HttpRequest):
    """Página inicial para buscas de disciplina_em_curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    context["resultados"] = []
    if filtro.isnumeric():
        response, curso = conn.consultar.curso(login.token, int(filtro)) #disciplinas
        context["resultados"] = curso.disciplinas
        
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_disciplina_em_curso.html", context), login)

def procurar_aluno_em_curso(request: HttpRequest):
    """Página inicial para buscas de curso_matriculado"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, curso_matriculado = conn.procurar.curso_matriculado(login.token, filtro)
    context["resultados"] = curso_matriculado
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_aluno_em_curso.html", context), login)

def editar_professor_em_turma(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, dm = conn.consultar.disciplina_ministrada(login.token, id)
        context["cadastro"] = dm
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_professor_em_turma.html", context), login)

def professor_em_turma_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False}

    professor = conn.consultar.professor(login.token, request.GET.get("id_professor", ""))
    turma = conn.consultar.turma(login.token, request.GET.get("id_turma", ""))
    disciplina = conn.consultar.disciplina(login.token, request.GET.get("id_disciplina", ""))
    obj = api.Disciplina_Ministrada(
        disciplina=disciplina,
        professor=professor,
        turma=turma,
        encerrada=request.GET.get("encerrada", ""),
        coordenador=request.GET.get("coordenador", "")
    )

    if id == "":
        response = conn.cadastrar.analistarh(login.token, obj)
    else:
        response = conn.editar.analistarh(login.token, id, obj)
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["409"] = True
    return set_cookies(render(request, "analistarh/info_analista.html", context), login)


def editar_disciplina_em_curso(request: HttpRequest):
    pass

def editar_aluno_em_curso(request: HttpRequest):
    pass