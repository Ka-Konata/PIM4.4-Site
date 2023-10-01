from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request):
    """Retorna a página padrão para o usuário realizar o login."""
    context = {
        "erros": {"vazio":[]}
    }
    return render(request, "login/index.html", context)

def logar(request: HttpRequest):
    """Para ser usada em uma tag form, retorna o token e o refresh_token caso validado."""
    # Pegando os parâmetros na query
    id = request.GET.get("id", "")
    senha = request.GET.get("senha", "")

    # Validando os parâmetros
    erros = {"vazio":[]}
    if id == "" or not id.isnumeric():
        erros["vazio"].append("id")
    if senha == "":
        erros["vazio"].append("senha")
    
    context = {
        "erros": erros
    }
    return render(request, "login/index.html", context)

def refresh_token(request, id, senha):
    """Retorna um novo token para garantir que o usuário continue logado (caso o refresh_token seja válido)."""
    return HttpResponse("GET refrsh_token")
