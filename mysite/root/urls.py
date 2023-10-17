from django.urls import path
from . import views

app_name = "root"

"""Configurando as urls para a página root"""
urlpatterns = [
    path("", views.index, name="index")
]
