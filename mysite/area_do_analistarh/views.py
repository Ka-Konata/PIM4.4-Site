import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils

conn = api.Connection(os.environ["API_URL"])

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Analista de RH"""
    # Tentando pegar os cookies.
    try:
        token = request.COOKIES[os.environ['API_TOKEN']]
        refresh_token = request.COOKIES[os.environ['API_REFRESH_TOKEN']]
        id = int(request.COOKIES[os.environ['API_USER_ID']])
    except:
        return redirect("login:index")

    # Fazendo o request na API
    response, analistarh = conn.consultar.analistarh(id, token)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Caso o refresh_token também seja inválido.
        if response.status_code == 400:
            return redirect("login:index")

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403:
        return render(request, "erros/403.html", context)

    # Adicionando o obj ao contexto e respondendo o request.
    context["analistarh"] = analistarh
    return render(request, "area_do_analistarh/index.html", context)