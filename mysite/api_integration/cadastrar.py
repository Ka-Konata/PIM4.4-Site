import requests
from . utils import *

class Cadastrar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, obj: object, url: str) -> requests.Response:
        # Preparando e efetuando o request na API.
        url = self.base_url + f"/{url}"
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.post(url, headers=headers, data=dict_to_josn(obj.to_dict()))
        return response

    def analistarh(self, token: str, analistarh: object) -> requests.Response:
        """Retorna umã lista de objetos do tipo AnalistaRH.
        param analistarh: api.AnalistaRH
        Return: list() [requests.Response, list() [AnalistaRH]]"""
        return self.__do_request(token, analistarh, self.URLs.ANALISTARH)

    def secretario(self, token: str, secretario: object) -> requests.Response:
        """Retorna umã lista de objetos do tipo Secretario.
        param secretario: api.Secretario
        Return: list() [requests.Response, list() [Secretario]]"""
        return self.__do_request(token, secretario, self.URLs.SECRETARIO)

    def professor(self, token: str, professor: object) -> requests.Response:
        """Retorna umã lista de objetos do tipo Professor.
        param professor: api.Professor
        Return: list() [requests.Response, list() [Professor]]"""
        return self.__do_request(token, professor, self.URLs.PROFESSOR)

    def aluno(self, token: str, aluno: object) -> requests.Response:
        """Retorna umã lista de objetos do tipo Aluno.
        param aluno: api.Aluno
        Return: list() [requests.Response, list() [Aluno]]"""
        return self.__do_request(token, aluno, self.URLs.ALUNO)

    def conteudo(self, token: str, id_disciplina_ministrada: int = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Conteudo.
        Return: list() [requests.Response, list() [Conteudo]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.CONTEUDO, self.Models.CONTEUDO, "idDisciplinaMinistrada", id_disciplina_ministrada)
    
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
