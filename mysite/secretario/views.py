import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils
from login.views import is_logged

conn = api.Connection(os.environ["API_URL"])

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do Secretario"""
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
    response, secretario = conn.consultar.secretario(token, id)
    context = {
        "erros":[]
    }
    
    r1, curso = conn.consultar.curso(token, 10001)
    r1, disciplina = conn.consultar.disciplina(token, 10001)
    
    # r = conn.cadastrar.disciplina_em_curso(token, curso.id, disciplina.id)
    # print(r.status_code, f"content: {r.text}")
    
    r = conn.apagar.disciplina_em_curso(token, curso.id, disciplina.id)
    print(f"------- {r.status_code}", f"content: {r.text}")

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Caso o refresh_token também seja inválido.
        if response.status_code == 400:
            return redirect("login:index")

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or cargo != utils.Cargo.SECRETARIO:
        return render(request, "erros/403.html", context)

    # Adicionando o obj ao contexto e respondendo o request.
    context["secretario"] = secretario
    return render(request, "secretario/index.html", context)
