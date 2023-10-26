from django.urls import path
from . import views

app_name = "erros"

"""Configurando as urls para a página de Erros"""
urlpatterns = [
    path("403", views.error403, name="403")
]
