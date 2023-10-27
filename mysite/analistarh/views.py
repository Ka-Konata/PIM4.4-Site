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
    response, analistarh = conn.consultar.analistarh(login.token, login.id)
    context = {
        "erros":[]
    }
    print("area status code:", response.status_code)

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Verificando se o refresh_token é válido
        refresh = conn.refresh(login.id, login.token, login.refresh_token)
        if refresh.status_code == 400:
            return redirect("login:index"), login

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.ANALISTARH:
        return redirect("erros:403"), login
    
    # Caso tudo ocorra bem
    context["analistarh"] = analistarh
    return context, login

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Analista de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/index.html", context), login)

def manter_analista(request: HttpRequest):
    """Página inicial para buscas de Analista de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    context["resultado"] = list()
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/manter_analista.html", context), login)

def procurar_analista(request: HttpRequest):
    """Página inicial para buscas de Analista de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, analistasrh = conn.procurar.analistarh(login.token, filtro)
    context["resultados"] = analistasrh
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/manter_analista.html", context), login)

def editar_analista(request: HttpRequest):
    pass
