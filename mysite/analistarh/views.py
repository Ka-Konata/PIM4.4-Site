import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils
from login.views import is_logged, Cookies

conn = api.Connection(os.environ["API_URL"])

def check_login(request: HttpRequest) -> [dict, Cookies]:
    # Verificando se o usuário está logado.
    if not is_logged(request):
        return redirect("login:index"), None
    
    # Tentando pegar os cookies.
    try:
        cookies = Cookies()
        cookies.token = request.COOKIES[os.environ['API_TOKEN']]
        cookies.refresh_token = request.COOKIES[os.environ['API_REFRESH_TOKEN']]
        cookies.id = int(request.COOKIES[os.environ['API_USER_ID']])
        cookies.cargo = request.COOKIES[os.environ['API_USER_CARGO']]
    except:
        return redirect("login:index"), None

    # Fazendo o request na API
    response, analistarh = conn.consultar.analistarh(cookies.token, id)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Caso o refresh_token também seja inválido.
        if response.status_code == 400:
            return redirect("login:index"), None

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or cookies.cargo != utils.Cargo.ANALISTARH:
        return render(request, "erros/403.html", context), None
    context["analistarh"] = analistarh
    print(context)
    return context, cookies

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Analista de RH"""
    context, cookies = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return render(request, "analistarh/index.html", context)

def manter_analista(request: HttpRequest):
    """Página inicial para buscas de Analista de RH"""
    context, cookies = check_login(request)
    if not isinstance(context, dict):
        return context
    
    context["resultado"] = list()
    
    # Adicionando o obj ao contexto e respondendo o request.
    return render(request, "analistarh/manter_analista.html", context)

def procurar_analista(request: HttpRequest):
    """Página inicial para buscas de Analista de RH"""
    context, cookies = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, analistasrh = conn.procurar.analistarh(cookies.token, filtro)
    context["resultados"] = analistasrh
    
    # Adicionando o obj ao contexto e respondendo o request.
    return render(request, "analistarh/manter_analista.html", context)

def editar_analista(request: HttpRequest):
    pass
