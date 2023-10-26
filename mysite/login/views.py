import os
import sys
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from api_integration import api, utils

# Fazendo conexão com o banco de dados.
conn = api.Connection(os.environ["API_URL"])

# Fazendo o cadastro inicial caso necessário
first_user = api.AnalistaRH(
    nome=os.environ["FIRST_USER_NAME"],
    cpf=int(os.environ["FIRST_USER_CPF"]),
    rg=int(os.environ["FIRST_USER_RG"]),
    telefone=int(os.environ["FIRST_USER_TELEFONE"]),
    email=os.environ["FIRST_USER_EMAIL"]
)
response = conn.startup(first_user)

if response.status_code == 200:
    input("AVISO: foi efetuada a criação da conta inicial no banco de dados (StartUp). Os dados utilizados para criação desta conta podem ser vizualidados no arquivo .env caso exista.\nPressione ENTER para continuar...")

# Create your views here.

def index(request):
    """Retorna a página padrão para o usuário realizar o login."""
    # Verificando se o usuário já está conectado, e redirecionando caso a resposta for sim.
    logged, login = is_logged(request)
    print(f"is logged? {logged} | id: {login.id} | cargo: {login.cargo}")
    if logged:
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
    if id == "":
        erros["vazio"].append("id")
    if senha == "":
        erros["vazio"].append("senha")
    elif not id.isnumeric():
        erros["401"] = True

    # Fazendo um request na API para efetuar o login.
    if len(erros["vazio"]) == 0 and not erros["401"]:
        response = conn.login(id, senha)

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
            r = set_cookies(r, login)
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
    return set_cookies(redirect("login:index"), api.Login())


def get_cargo_redirect(request_or_str, is_request: bool = False) -> HttpResponseRedirect:
    if is_request:
        cargo = request_or_str.COOKIES[os.environ['API_USER_CARGO']]
    else:
        cargo = request_or_str
    return redirect(f"{cargo.lower()}:index")


def is_logged(request: HttpRequest) -> [bool, api.Login]:
    """Verifique se um usuário está logado ou não.
    \nCaso esteja logado, retorna um HttpResponseRedirect para a sua respectiva área.
    \nCaso contrário, retorna None."""
    # Tentando instanciar um objeto do tipo Login.
    login = api.Login()
    try:
        login.token = request.COOKIES[os.environ['API_TOKEN']]
        login.refresh_token = request.COOKIES[os.environ['API_REFRESH_TOKEN']]
        login.cargo = request.COOKIES[os.environ['API_USER_CARGO']]
        login.id = int(request.COOKIES[os.environ['API_USER_ID']])
    except Exception as e:
        return False, login
    
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
        return False, login
    
    print(response.status_code)
    # Resultado da requisição.
    if response.status_code == 401:
        # Verificando se o refresh_token é válido
        refresh = conn.refresh(login.id, login.token, login.refresh_token)
        print(refresh.status_code)
        if refresh.status_code == 400:
            return False, login
    
    # Caso tenha passado por todas as validações.
    return True, login

def set_cookies(r: HttpResponse, login: api.Login) -> HttpResponse:
    expires = datetime.utcnow() + timedelta(days=7)
    r.set_cookie(os.environ["API_TOKEN"], login.token, expires=expires)
    r.set_cookie(os.environ["API_REFRESH_TOKEN"], login.refresh_token, expires=expires)
    r.set_cookie(os.environ["API_USER_CARGO"], login.cargo, expires=expires)
    r.set_cookie(os.environ["API_USER_ID"], login.id, expires=expires)
    return r