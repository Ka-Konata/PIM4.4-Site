import requests
from . utils import *

class Apagar:
    """Classe para realizar exclusões na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, id: int, url: str, model: any) -> requests.Response:
        # Preparando e efetuando o request na API.
        url = self.base_url + f"/{url}/{id}"
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"
        return requests.delete(url, headers=headers)

    def analistarh(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto AnalistaRH.
        Return: list() [requests.Response, AnalistaRH]"""
        return self.__do_request(token, id, self.URLs.ANALISTARH, self.Models.ANALISTARH)

    def secretario(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Secretario.
        Return: list() [requests.Response, Secretario]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.SECRETARIO, self.Models.SECRETARIO)

    def professor(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Professor.
        Return: list() [requests.Response, Professor]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.PROFESSOR, self.Models.PROFESSOR)

    def aluno(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Aluno.
        Return: list() [requests.Response, Aluno]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.ALUNO, self.Models.ALUNO)

    def conteudo(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Conteudo.
        Return: list() [requests.Response, Conteudo]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CONTEUDO, self.Models.CONTEUDO)

    def curso_matriculado(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Curso_Matriculado.
        Return: list() [requests.Response, Curso_Matriculado]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO_MATRICULADO, self.Models.CURSO_MATRICULADO)

    def curso(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Curso.
        Return: list() [requests.Response, Curso]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO, self.Models.CURSO)

    def disciplina_cursada(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Disciplina_Cursada.
        Return: list() [requests.Response, Disciplina_Cursada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_CURSADA, self.Models.DISCIPLINA_CURSADA)

    def disciplina_ministrada(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Disciplina_Ministrada.
        Return: list() [requests.Response, Disciplina_Ministrada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_MINISTRADA, self.Models.DISCIPLINA_MINISTRADA)

    def disciplina(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Disciplina.
        Return: list() [requests.Response, Disciplina]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA, self.Models.DISCIPLINA)

    def turma(self, token: str, id: int) -> list[requests.Response, object]:
        """Retorna um objeto Turma.
        Return: list() [requests.Response, Turma]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.TURMA, self.Models.TURMA)
    
    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def base_headers(self):
        return self.__base_headers

    @property
    def URLs(self):
        return self.__URLs
    
    @property
    def Models(self):
        return self.__Models
