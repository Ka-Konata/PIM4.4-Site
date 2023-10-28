import os, json
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, FileResponse
from api_integration import api, utils
from login.views import is_logged, set_cookies

conn = api.Connection(os.environ["API_URL"])

def verificar_pasta_arquivos_temporarios():
    pasta = os.getcwd() + "\\arquivos_temporarios\\"
    if not os.path.isdir(pasta):
        os.mkdir(pasta)

def apagar_todos_os_arquivos_temporarios():
    pasta = os.getcwd() + "\\arquivos_temporarios\\"
    for file in os.listdir(pasta):
        os.remove(os.path.join(pasta, file))

def check_login(request: HttpRequest) -> [dict, api.Login]:
    # Verificando se o usuário está logado.
    logged, login = is_logged(request)
    if not logged:
        return redirect("login:index"), login

    # Fazendo o request na API
    response, aluno = conn.consultar.aluno(login.token, login.id)
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
        response, aluno = conn.consultar.aluno(login.token, login.id)

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.ALUNO:
        return redirect("erros:403"), login
    
    # Caso tudo ocorra bem
    context["aluno"] = aluno
    return context, login

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do aluno de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "aluno/index.html", context), login)

def acessar_cursos(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, cms = conn.procurar.curso_matriculado(login.token, login.id)
    context["resultados"] = []
    
    # Apenas os do aluno
    for cm in cms:
        if filtro in cm.curso.nome or filtro == "":
            context["resultados"].append(cm)
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "aluno/acessar_cursos.html", context), login)

def acessar_disciplinas(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    curso_matriculado = request.GET.get("curso_matriculado", "")
    response, dcs = conn.procurar.disciplina_cursada(login.token, curso_matriculado)
    context["resultados"] = []
    
    # Apenas os do aluno
    for dc in dcs:
        if filtro in dc.disciplina.nome or filtro == "":
            context["resultados"].append(dc)
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "aluno/acessar_disciplinas.html", context), login)

def acessar_conteudos(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    turma = request.GET.get("turma", "")
    disciplina = request.GET.get("disciplina", "")
    print(turma, disciplina)
    
    professores = conn.consultar.turma(login.token, turma)[1].professores 
    disciplina_ministrada = None
    for p in professores:
        dms = conn.procurar.disciplina_ministrada(login.token, p.id)[1]
        for dm in dms:
            if dm.disciplina.id == disciplina:
                disciplina_ministrada = dm.id
                
    conteudos = conn.procurar.conteudo(login.token, disciplina_ministrada)[1]
    for c in range(0, len(conteudos)):
        conteudos[c].documento_url = conteudos[c].documento_url.replace("/api/file/conteudo/", "")
    context["resultados"] = conteudos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "aluno/acessar_conteudos.html", context), login)

def download_conteudo(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    verificar_pasta_arquivos_temporarios()
    apagar_todos_os_arquivos_temporarios()
    file_path = os.path.join(os.getcwd() + "\\arquivos_temporarios\\", request.GET.get("file_name", ""))
    response = conn.arquivo.conteudo(login.token, request.GET.get("file_name", ""))

    filew = open(file_path, 'wb')
    filew.write(response.content)
    filew.close()

    return FileResponse(open(file_path, "rb"), as_attachment=True)

def notas_e_faltas(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    cms = conn.procurar.curso_matriculado(login.token, login.id)[1]
    context["resultados"] = []
    
    # Apenas os do curso
    for cm in cms:
        if filtro in cm.curso.nome or filtro == "":
            for d in cm.disciplinas:
                dcs = conn.procurar.disciplina_cursada(login.token, cm.id)[1]
                print(dcs)
                context["resultados"] += dcs
                print(context["resultados"])
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "aluno/notas_e_faltas.html", context), login)


def download_declaracao(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    verificar_pasta_arquivos_temporarios()
    apagar_todos_os_arquivos_temporarios()

    file_name = f"declaracao ({str(datetime.now())}).pdf"
    file_path = os.path.join(os.getcwd() + "\\arquivos_temporarios\\", file_name)
    response = conn.arquivo.declaracao(login.token, str(login.id))

    filew = open(file_path, 'wb')
    filew.write(response.content)
    filew.close()

    return FileResponse(open(file_path, "rb"), as_attachment=True)

def download_historico(request: HttpRequest):
    pass

def download_relatorio(request: HttpRequest):
    pass

def download_boletim(request: HttpRequest):
    pass