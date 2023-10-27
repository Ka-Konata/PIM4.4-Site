from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    # Redireciona para login
    return redirect("login:index")