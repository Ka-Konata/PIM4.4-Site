import requests
import json
from . models.analistarh import AnalistaRH
from . models.secretario import Secretario
from . models.professor import Professor
from . models.aluno import Aluno
from . utils import *
from django.http import HttpResponse

class Consultar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers

    def analistarh(self, id: int, token: str) -> list[HttpResponse, AnalistaRH]:
        """Retorna um objeto AnalistaRH.
        Return: list() [django.http.HttpResponse, AnalistaRH]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/analistarh/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe AnalistaRH.
        analistarh = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            analistarh = AnalistaRH.by_dict(r)
        return [response, analistarh]

    def secretario(self, id: int, token: str) -> list[HttpResponse, Secretario]:
        """Retorna um objeto Secretario.
        Return: list() [django.http.HttpResponse, Secretario]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/secretario/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Secretario.
        secretario = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            secretario = Secretario.by_dict(r)
        return [response, secretario]

    def professor(self, id: int, token: str) -> list[HttpResponse, Professor]:
        """Retorna um objeto Professor.
        Return: list() [django.http.HttpResponse, Professor]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/professor/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Professor.
        professor = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            professor = Professor.by_dict(r)
        return [response, professor]

    def aluno(self, id: int, token: str) -> list[HttpResponse, Aluno]:
        """Retorna um objeto Aluno.
        Return: list() [django.http.HttpResponse, Aluno]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/aluno/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Aluno.
        aluno = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            aluno = Aluno.by_dict(r)
        return [response, aluno]

