import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils
from login.views import is_logged

conn = api.Connection(os.environ["API_URL"])

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Analista de RH"""
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
    response, analistarh = conn.consultar.analistarh(token, id)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Caso o refresh_token também seja inválido.
        if response.status_code == 400:
            return redirect("login:index")

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or cargo != utils.Cargo.ANALISTARH:
        return render(request, "erros/403.html", context)

    # Adicionando o obj ao contexto e respondendo o request.
    context["analistarh"] = analistarh
    print("context: ", context)
    return render(request, "analistarh/index.html", context)

def manter_analista(request: HttpRequest):
    # Tentando pegar os cookies.
    try:
        token = request.COOKIES[os.environ['API_TOKEN']]
        refresh_token = request.COOKIES[os.environ['API_REFRESH_TOKEN']]
        id = int(request.COOKIES[os.environ['API_USER_ID']])
        cargo = request.COOKIES[os.environ['API_USER_CARGO']]
    except:
        return redirect("login:index")
    
    # Adicionando o obj ao contexto e respondendo o request.
    context = {}
    context["analistarh"] = "analistarh"
    return render(request, "analistarh/manter_analista.html", context)

def procurar_analista(request: HttpRequest):
    # Adicionando o obj ao contexto e respondendo o request.
    context = {}
    context["analistarh"] = "analistarh"
    return render(request, "analistarh/manter_analista.html", context)

def editar_analista(request: HttpRequest):
    pass
    