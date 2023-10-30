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
        
        # Caso o refresh tenha tido êxito
        login = api.Login()
        login.set_values_with_response(refresh)
        # Fazendo o request na API novamente com o novo token
        response, analistarh = conn.consultar.analistarh(login.token, login.id)

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

def procurar_secretario(request: HttpRequest):
    """Página inicial para buscas de secretario"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, secretarios = conn.procurar.secretario(login.token, filtro)
    context["resultados"] = secretarios
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/manter_secretario.html", context), login)

def procurar_professor(request: HttpRequest):
    """Página inicial para buscas de professor"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, professores = conn.procurar.professor(login.token, filtro)
    context["resultados"] = professores
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/manter_professor.html", context), login)

def editar_analista(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de AnalistaRH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, analistarh = conn.consultar.analistarh(login.token, id)
        context["cadastro"] = analistarh
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/info_analista.html", context), login)

def editar_professor(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de professor"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, professor = conn.consultar.professor(login.token, id)
        context["cadastro"] = professor
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/info_professor.html", context), login)

def editar_secretario(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de secretario"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, secretario = conn.consultar.secretario(login.token, id)
        context["cadastro"] = secretario
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "analistarh/info_secretario.html", context), login)

def analistarh_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.AnalistaRH(
        nome = request.GET.get("nome", ""),
        rg = int(request.GET.get("rg", "")),
        cpf = int(request.GET.get("cpf", "")),
        telefone = int(request.GET.get("telefone", "")),
        email = request.GET.get("email", "")
    )

    if id == "":
        response = conn.cadastrar.analistarh(login.token, obj)
    else:
        response = conn.editar.analistarh(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "analistarh/info_analista.html", context), login)

def secretario_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.Secretario(
        nome = request.GET.get("nome", ""),
        rg = int(request.GET.get("rg", "")),
        cpf = int(request.GET.get("cpf", "")),
        telefone = int(request.GET.get("telefone", "")),
        email = request.GET.get("email", "")
    )

    if id == "":
        response = conn.cadastrar.secretario(login.token, obj)
    else:
        response = conn.editar.secretario(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "analistarh/info_secretario.html", context), login)

def professor_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.Professor(
        nome = request.GET.get("nome", ""),
        rg = int(request.GET.get("rg", "")),
        cpf = int(request.GET.get("cpf", "")),
        telefone = int(request.GET.get("telefone", "")),
        email = request.GET.get("email", "")
    )

    if id == "":
        response = conn.cadastrar.professor(login.token, obj)
    else:
        response = conn.editar.professor(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "analistarh/info_professor.html", context), login)

def analistarh_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = conn.apagar.analistarh(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "analistarh/info_analista.html", context), login)

def secretario_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = conn.apagar.secretario(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "analistarh/info_secretario.html", context), login)

def professor_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = conn.apagar.professor(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "analistarh/info_professor.html", context), login)
