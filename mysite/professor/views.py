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
    response, professor = conn.consultar.professor(login.token, login.id)
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
        response, professor = conn.consultar.professor(login.token, login.id)

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.PROFESSOR:
        return redirect("erros:403"), login
    
    # Caso tudo ocorra bem
    context["professor"] = professor
    return context, login

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do professor de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/index.html", context), login)

def procurar_conteudo(request: HttpRequest):
    """Página inicial para buscas de conteudo"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, conteudos = conn.procurar.conteudo(login.token, filtro)
    context["resultados"] = conteudos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/manter_conteudo.html", context), login)

def editar_conteudo(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de conteudo"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, conteudo = conn.consultar.conteudo(login.token, id)
        context["cadastro"] = conteudo
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/info_conteudo.html", context), login)

def acessar_disciplinas(request: HttpRequest):
    """Página inicial para buscas de disciplina"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplinas = conn.procurar.disciplina_ministrada(login.token, login.id)

    resultados = []
    for d in disciplinas:
        # print(f"filtro: {filtro} | disciplina: {d.turma.nome}", filtro in d.turma.nome)
        if filtro in d.turma.nome or filtro == "":
            resultados.append(d)

    context["resultados"] = resultados
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/acessar_disciplina.html", context), login)

def acessar_alunos_em_disciplinas(request: HttpRequest):
    """Página inicial para buscas de alunos_em_disciplinas"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    disciplina = request.GET.get("disciplina", "")
    curso = request.GET.get("curso", "")
    filtro = request.GET.get("filtro", "")

    resultados = []
    r2, disciplinas_cursadas = conn.procurar.disciplina_cursada(login.token)
    for dc in disciplinas_cursadas:
        # print(f"disciplina: {str(dc.disciplina.id)} == {disciplina}: {str(dc.disciplina.id) == disciplina}")
        # print(f"curso: {str(dc.curso_matriculado.curso.id)} == {curso}: {str(dc.curso_matriculado.curso.id) == curso}")
        # print(f"filtro: {str(dc.disciplina.id)} in {dc.curso_matriculado.aluno.nome}: {filtro in dc.curso_matriculado.aluno.nome}")
        # print(f"filtro: {filtro} == : {filtro == ''}")
        if str(dc.disciplina.id) == disciplina and str(dc.curso_matriculado.curso.id) == curso and (filtro in dc.curso_matriculado.aluno.nome or filtro == ""):
            resultados.append(dc.curso_matriculado.aluno)

    context["disciplina"] = disciplina
    context["curso"] = curso
    context["resultados"] = resultados
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/alunos_em_disciplina.html", context), login)

def mapa_de_notas(request: HttpRequest):
    """Página inicial para buscas de disciplina"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplinas_cursadas = conn.procurar.disciplina_cursada(login.token)

    resultados = []
    for dc in disciplinas_cursadas:
        if filtro == str(dc.disciplina.id) or filtro == "":
            resultados.append(dc)

    context["resultados"] = resultados
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "professor/mapa_de_notas.html", context), login)
