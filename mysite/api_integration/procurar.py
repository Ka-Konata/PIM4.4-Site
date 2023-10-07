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

class Procurar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict, url_list, classes_list) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__url_list = url_list
        self.__classes_list = classes_list

    def __do_request(self, token: str, tipo: str, filtro_nome: str = None, filtro_value = None) -> list[requests.Response, list[AnalistaRH]]:
        # Preparando e efetuando o request na API.
        url = self.base_url + f"/{self.__url_list[tipo]}"
        if filtro_nome != None and filtro_value != None:
            url = url + f"?{filtro_nome}={filtro_value}"
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        classe = self.__classes_list[tipo]

        # Instanciando o objeto da classe.
        objs = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for obj in r:
                objs.append(classe.by_dict(obj))
        return [response, objs]

    def analistarh(self, token: str, nome: str) -> list[requests.Response, list[AnalistaRH]]:
        """Retorna umã lista de objetos do tipo AnalistaRH.
        Return: list() [requests.Response, list() [AnalistaRH]]"""
        return self.__do_request(token, "analistarh", "nome", nome)

    def secretario(self, token: str, nome: str) -> list[requests.Response, list[Secretario]]:
        """Retorna umã lista de objetos do tipo Secretario.
        Return: list() [requests.Response, list() [Secretario]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, "secretario", "nome", nome)

    def professor(self, token: str, nome: str) -> list[requests.Response, list[Professor]]:
        """Retorna umã lista de objetos do tipo Professor.
        Return: list() [requests.Response, list() [Professor]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, "professor", "nome", nome)

    def aluno(self, token: str, nome: str) -> list[requests.Response, list[Aluno]]:
        """Retorna umã lista de objetos do tipo Aluno.
        Return: list() [requests.Response, list() [Aluno]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, "aluno", "nome", nome)

    def conteudo(self, token: str) -> list[requests.Response, list[Conteudo]]:
        """Retorna umã lista de objetos do tipo Conteudo.
        Return: list() [requests.Response, list() [Conteudo]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, "conteudo")
    
    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def base_headers(self):
        return self.__base_headers
