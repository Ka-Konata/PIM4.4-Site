from django.urls import path
from . import views

app_name = "secretario"

"""Configurando as urls para a página de login"""
urlpatterns = [
    path("", views.index, name="index")
]
