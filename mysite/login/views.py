import os
import sys
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from api_integration import api, utils

# Fazendo conexão com o banco de dados.
conn = api.Connection(os.environ["API_URL"])

# Create your views here.

def index(request):
    """Retorna a página padrão para o usuário realizar o login."""
    # Verificando se o usuário já está conectado, e redirecionando caso a resposta for sim.
    print(f"is logged? {is_logged(request)}")
    if is_logged(request):
        return get_cargo_redirect(request, True)
    
    # Retornando a página de login.
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
            login = utils.Login()
            login.set_values_with_response(response)

            # Verificando o tipo de conta
            if login.cargo in utils.Cargo.TODOS:
                r = get_cargo_redirect(login.cargo)
            else:
                r = HttpResponse(f"id: {login.id}<br>token: {login.token}<br>refresh_token: {login.refresh_token}")

            # Montando o HttpResponse. (MUDAR PARA PÁGINS DPS)
            expires = datetime.utcnow() + timedelta(days=7)
            r.set_cookie(os.environ["API_TOKEN"], login.token, expires=expires)
            r.set_cookie(os.environ["API_REFRESH_TOKEN"], login.refresh_token, expires=expires)
            r.set_cookie(os.environ["API_USER_CARGO"], login.cargo, expires=expires)
            r.set_cookie(os.environ["API_USER_ID"], login.id, expires=expires)
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
    print(context)
    return render(request, "mudar_senha/index.html", context)


def refresh_token(request, id, senha):
    """Retorna um novo token para garantir que o usuário continue logado (caso o refresh_token seja válido)."""
    return HttpResponse("GET refrsh_token")


def sair(request):
    # Montando o HttpResponse. (MUDAR PARA PÁGINS DPS)
    expires = datetime.utcnow() + timedelta(days=7)
    r = redirect("login:index")
    r.set_cookie(os.environ["API_TOKEN"], "", expires=expires)
    r.set_cookie(os.environ["API_REFRESH_TOKEN"], "", expires=expires)
    r.set_cookie(os.environ["API_USER_CARGO"], "", expires=expires)
    r.set_cookie(os.environ["API_USER_ID"], "", expires=expires)
    return r


def get_cargo_redirect(request_or_str, is_request: bool = False) -> HttpResponseRedirect:
    if is_request:
        cargo = request_or_str.COOKIES[os.environ['API_USER_CARGO']]
    else:
        cargo = request_or_str
    return redirect(f"{cargo.lower()}:index")


def is_logged(request: HttpRequest) -> bool:
    """Verifique se um usuário está logado ou não.
    \nCaso esteja logado, retorna um HttpResponseRedirect para a sua respectiva área.
    \nCaso contrário, retorna None."""
    # Tentando instanciar um objeto do tipo Login.
    try:
        login = api.Login(
            token=request.COOKIES[os.environ['API_TOKEN']],
            refresh_token=request.COOKIES[os.environ['API_REFRESH_TOKEN']],
            cargo=request.COOKIES[os.environ['API_USER_CARGO']],
            id=int(request.COOKIES[os.environ['API_USER_ID']])
        )
    except Exception as e:
        return False
    
    # Verificando o cargo do usuário em questão.
    if login.cargo == utils.Cargo.ANALISTARH:
        response, analistarh = conn.consultar.analistarh(login.token, login.id)
    elif login.cargo == utils.Cargo.SECRETARIO:
        response, secretario = conn.consultar.secretario(login.token, login.id)
    elif login.cargo == utils.Cargo.PROFESSOR:
        response, professor = conn.consultar.professor(login.token, login.id)
    elif login.cargo == utils.Cargo.ALUNO:
        response, aluno = conn.consultar.aluno(login.token, login.id)
    else:
        return False
    
    # Resultado da requisição.
    #print(response.status_code)
    if response.status_code != 200:
        return False
    
    # Caso tenha passado por todas as validações.
    return True

class Cookies:
    token = None
    refresh_token = None
    id = None
    cargo = None