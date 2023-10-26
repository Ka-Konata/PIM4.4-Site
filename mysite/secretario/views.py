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
    if response.status_code == 401 or response.status_code:
        # Verificando se o refresh_token é válido
        refresh = conn.refresh(login.id, login.token, login.refresh_token)
        if refresh.status_code == 400:
            return redirect("login:index"), login

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.secretario:
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
