import requests
import json
from django.http import HttpResponse
from . models.analistarh import AnalistaRH
from . models.secretario import Secretario
from . models.professor import Professor
from . models.aluno import Aluno
from . models.conteudo import Conteudo
from . models.curso_matriculado import Curso_Matriculado
from . models.curso import Curso
from . models.disciplina_cursada import Disciplina_Cursada
from . models.disciplina_ministrada import Disciplina_Ministrada
from . models.disciplina import Disciplina
from . models.turma import Turma
from . utils import *

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

    def conteudo(self, id: int, token: str) -> list[HttpResponse, Conteudo]:
        """Retorna um objeto Conteudo.
        Return: list() [django.http.HttpResponse, Conteudo]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/conteudo/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Conteudo.
        conteudo = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            conteudo = Conteudo.by_dict(r)
        return [response, conteudo]

    def curso_matriculado(self, id: int, token: str) -> list[HttpResponse, Curso_Matriculado]:
        """Retorna um objeto Curso_Matriculado.
        Return: list() [django.http.HttpResponse, Curso_Matriculado]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/cursoMatriculado/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Curso_Matriculado.
        curso_matriculado = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            curso_matriculado = Curso_Matriculado.by_dict(r)
        return [response, curso_matriculado]

    def curso(self, id: int, token: str) -> list[HttpResponse, Curso]:
        """Retorna um objeto Curso.
        Return: list() [django.http.HttpResponse, Curso]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/curso/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Curso.
        curso = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            curso = Curso.by_dict(r)
        return [response, curso]

    def disciplina_cursada(self, id: int, token: str) -> list[HttpResponse, Disciplina_Cursada]:
        """Retorna um objeto Disciplina_Cursada.
        Return: list() [django.http.HttpResponse, Disciplina_Cursada]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/disciplinaCursada/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Disciplina_Cursada.
        disciplina_cursada = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            disciplina_cursada = Disciplina_Cursada.by_dict(r)
        return [response, disciplina_cursada]

    def disciplina_ministrada(self, id: int, token: str) -> list[HttpResponse, Disciplina_Ministrada]:
        """Retorna um objeto Disciplina_Ministrada.
        Return: list() [django.http.HttpResponse, Disciplina_Ministrada]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/disciplinaMinistrada/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Disciplina_Ministrada.
        disciplina_ministrada = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            disciplina_ministrada = Disciplina_Ministrada.by_dict(r)
        return [response, disciplina_ministrada]

    def disciplina(self, id: int, token: str) -> list[HttpResponse, Disciplina]:
        """Retorna um objeto Disciplina.
        Return: list() [django.http.HttpResponse, Disciplina]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/disciplina/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Disciplina.
        disciplina = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            disciplina = Disciplina.by_dict(r)
        return [response, disciplina]

    def turma(self, id: int, token: str) -> list[HttpResponse, Turma]:
        """Retorna um objeto Turma.
        Return: list() [django.http.HttpResponse, Turma]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/turma/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Turma.
        turma = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            turma = Turma.by_dict(r)
        return [response, turma]
