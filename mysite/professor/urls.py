from django.urls import path
from . import views

app_name = "professor"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("conteudo", views.conteudo, name="conteudo")
]
