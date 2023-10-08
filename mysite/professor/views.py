import os, json
from django.shortcuts import render, redirect
from django.http import *
from api_integration import api, utils
from login.views import is_logged

conn = api.Connection(os.environ["API_URL"])

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Professor"""
    # Verificando se o usuário está logado.
    if not is_logged(request):
        return redirect("login:index")
    
    # Tentando pegar os cookies.
    try:
        token = request.COOKIES[os.environ['API_TOKEN']]
        refresh_token = request.COOKIES[os.environ['API_REFRESH_TOKEN']]
        id = int(request.COOKIES[os.environ['API_USER_ID']])
        cargo = request.COOKIES[os.environ['API_USER_CARGO']]
    except:
        return redirect("login:index")

    # Fazendo o request na API
    response, professor = conn.consultar.professor(token, id)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Caso o refresh_token também seja inválido.
        if response.status_code == 400:
            return redirect("login:index")

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or cargo != utils.Cargo.PROFESSOR:
        return render(request, "erros/403.html", context)

    # Adicionando o obj ao contexto e respondendo o request.
    context["professor"] = professor
    return render(request, "professor/index.html", context)

def conteudo(request: HttpRequest):
    id_dm = request.POST["id"]
    file = request.FILES["file"]
    token = request.COOKIES[os.environ['API_TOKEN']]
    
    disciplina_ministrada = api.Disciplina_Ministrada(id=id_dm)
    conteudo = api.Conteudo(disciplina_ministrada=disciplina_ministrada, documento=file)
    r = conn.cadastrar.conteudo(token, conteudo)
    print(r.status_code, f"headers: {r.headers}", f"content: {r.content}")
    return redirect("professor:index")
