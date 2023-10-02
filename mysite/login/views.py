import os
import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils

conn = api.Connection(os.environ["API_URL"])

# Create your views here.

def index(request):
    """Retorna a página padrão para o usuário realizar o login."""
    context = {
        "erros": {"vazio":[]}
    }
    return render(request, "login/index.html", context)


def connect(request: HttpRequest) -> HttpResponse:
    """Para ser usada em uma tag form, retorna o token e o refresh_token caso validado."""
    # Pegando os parâmetros na query.
    id = request.GET.get("id", "")
    senha = request.GET.get("senha", "")

    # Validando os parâmetros.
    erros = {"vazio":[], "401":False, "426":False}
    if id == "" or not id.isnumeric():
        erros["vazio"].append("id")
    if senha == "":
        erros["vazio"].append("senha")

    # Fazendo um request na API para efetuar o login.
    if len(erros["vazio"]) == 0:
        response = conn.login(int(id), senha)

        # Validando o resultado.
        if response.status_code == 200: # OK
            login = utils.Login(response)

            # Verificando o tipo de conta
            if login.cargo == "AnalistaRH":
                r = redirect("area_do_analistarh:index")
            else:
                r = HttpResponse(f"id: {login.id}<br>token: {login.token}<br>refresh_token: {login.refresh_token}")

            # Montando o HttpResponse. (MUDAR PARA PÁGINS DPS)
            r.set_cookie(os.environ["API_TOKEN"], login.token)
            r.set_cookie(os.environ["API_REFRESH_TOKEN"], login.refresh_token)
            r.set_cookie(os.environ["API_USER_CARGO"], login.cargo)
            r.set_cookie(os.environ["API_USER_ID"], login.id)
            return r
        
        elif response.status_code == 401: # Unauthorized
            erros["401"] = True
        
        elif response.status_code == 426: # UpgradeRequired
            erros["426"] = True

    # Renderizando a página html
    context = {
        "erros": erros
    }
    return render(request, "login/index.html", context)

def index_mudar_senha(request):
    """Retorna a página padrão para o usuário realizar o login."""
    context = {
        "erros": {"vazio":[]}
    }
    return render(request, "mudar_senha/index.html", context)


def mudar_senha(request) -> HttpResponse:
    """Mudar a senha de uma conta."""
    # Pegando os parâmetros na query.
    id = request.GET.get("id", "")
    senha_antiga = request.GET.get("senha_antiga", "")
    senha_nova = request.GET.get("senha_nova", "")

    # Validando os parâmetros.
    erros = {"vazio":[], "400":False, "401":False}
    if id == "" or not id.isnumeric():
        erros["vazio"].append("id")
    if senha_antiga == "":
        erros["vazio"].append("senha_antiga")
    if senha_nova == "":
        erros["vazio"].append("senha_nova")

    # Fazendo um request na API para efetuar o login.
    if len(erros["vazio"]) == 0:
        response = conn.mudar_senha(int(id), senha_antiga, senha_nova)

        # Validando o resultado.
        if response.status_code == 200: # OK
            # Montando o HttpResponse. (MUDAR PARA PÁGINS DPS)
            return redirect("login:index")
        
        elif response.status_code == 400: # BadRequest
            erros["400"] = True
        
        elif response.status_code == 401: # Unauthorized
            erros["401"] = True

    # Renderizando a página html
    context = {
        "erros": erros
    }
    return render(request, "mudar_senha/index.html", context)


def refresh_token(request, id, senha):
    """Retorna um novo token para garantir que o usuário continue logado (caso o refresh_token seja válido)."""
    return HttpResponse("GET refrsh_token")


def sair(request):
    # Montando o HttpResponse. (MUDAR PARA PÁGINS DPS)
    r = redirect("login:index")
    r.set_cookie(os.environ["API_TOKEN"], "")
    r.set_cookie(os.environ["API_REFRESH_TOKEN"], "")
    r.set_cookie(os.environ["API_USER_CARGO"], "")
    r.set_cookie(os.environ["API_USER_ID"], "")
    return r
