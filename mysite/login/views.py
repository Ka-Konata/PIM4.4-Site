from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {"test_bool": True, "test_list": [100, 200, 300, 400, 500]}
    return render(request, "login/index.html", context)

def login(request, id, senha):
    # Ainda para implementar
    return HttpResponse("GET login")

def refresh_token(request, id, senha):
    # Ainda para implementar
    return HttpResponse("GET refrsh_token")
