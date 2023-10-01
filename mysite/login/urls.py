from django.urls import path
from . import views

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index"),
    path("logar", views.logar, name="logar") #"^(?P<id>[\w-]+)/$"
]
