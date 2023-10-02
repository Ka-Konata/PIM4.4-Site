from django.urls import path
from . import views

app_name = "login"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("connect", views.connect, name="connect"), #"^(?P<id>[\w-]+)/$"
    path("mudar_senha", views.index_mudar_senha, name="mudar_senha_pag"),
    path("mudar_senha/mudar", views.mudar_senha, name="mudar_senha"),
    path("sair", views.sair, name="sair")
]
