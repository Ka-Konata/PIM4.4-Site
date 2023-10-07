import requests
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
    def __init__(self, base_url: str, base_headers: dict, url_list: dict, classes_list: dict) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__url_list = url_list
        self.__classes_list = classes_list

    def __do_request(self, token: str, id: int, tipo: str) -> list[requests.Response, any]:
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/{self.__url_list[tipo]}/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe.
        obj = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            obj = self.__classes_list[tipo].by_dict(r)
        return [response, obj]


    def analistarh(self, token: str, id: int) -> list[requests.Response, AnalistaRH]:
        """Retorna um objeto AnalistaRH.
        Return: list() [requests.Response, AnalistaRH]"""
        return self.__do_request(token, id, "analistarh")

    def secretario(self, token: str, id: int) -> list[requests.Response, Secretario]:
        """Retorna um objeto Secretario.
        Return: list() [requests.Response, Secretario]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "secretario")

    def professor(self, token: str, id: int) -> list[requests.Response, Professor]:
        """Retorna um objeto Professor.
        Return: list() [requests.Response, Professor]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "professor")

    def aluno(self, token: str, id: int) -> list[requests.Response, Aluno]:
        """Retorna um objeto Aluno.
        Return: list() [requests.Response, Aluno]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "aluno")

    def conteudo(self, token: str, id: int) -> list[requests.Response, Conteudo]:
        """Retorna um objeto Conteudo.
        Return: list() [requests.Response, Conteudo]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "conteudo")

    def curso_matriculado(self, token: str, id: int) -> list[requests.Response, Curso_Matriculado]:
        """Retorna um objeto Curso_Matriculado.
        Return: list() [requests.Response, Curso_Matriculado]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "curso_matriculado")

    def curso(self, token: str, id: int) -> list[requests.Response, Curso]:
        """Retorna um objeto Curso.
        Return: list() [requests.Response, Curso]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "curso")

    def disciplina_cursada(self, token: str, id: int) -> list[requests.Response, Disciplina_Cursada]:
        """Retorna um objeto Disciplina_Cursada.
        Return: list() [requests.Response, Disciplina_Cursada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "disciplina_cursada")

    def disciplina_ministrada(self, token: str, id: int) -> list[requests.Response, Disciplina_Ministrada]:
        """Retorna um objeto Disciplina_Ministrada.
        Return: list() [requests.Response, Disciplina_Ministrada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "disciplina_ministrada")

    def disciplina(self, token: str, id: int) -> list[requests.Response, Disciplina]:
        """Retorna um objeto Disciplina.
        Return: list() [requests.Response, Disciplina]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "disciplina")

    def turma(self, token: str, id: int) -> list[requests.Response, Turma]:
        """Retorna um objeto Turma.
        Return: list() [requests.Response, Turma]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, "turma")
