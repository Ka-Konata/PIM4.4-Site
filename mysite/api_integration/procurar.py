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
    def __init__(self, base_url: str, base_headers: dict) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers

    def analistarh(self, token: str, nome: str) -> list[requests.Response, list[AnalistaRH]]:
        """Retorna umã lista de objetos do tipo AnalistaRH.
        Return: list() [requests.Response, list() [AnalistaRH]]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/analistarh?nome={nome}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe AnalistaRH.
        analistarhs = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for analistarh in r:
                analistarhs.append(AnalistaRH.by_dict(analistarh))
        return [response, analistarhs]

    def secretario(self, token: str, nome: str) -> list[requests.Response, list[Secretario]]:
        """Retorna umã lista de objetos do tipo Secretario.
        Return: list() [requests.Response, list() [Secretario]]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/secretario?nome={nome}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Secretario.
        secretarios = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for secretario in r:
                secretarios.append(Secretario.by_dict(secretario))
        return [response, secretarios]

    def professor(self, token: str, nome: str) -> list[requests.Response, list[Professor]]:
        """Retorna umã lista de objetos do tipo Professor.
        Return: list() [requests.Response, list() [Professor]]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/professor?nome={nome}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Professor.
        professores = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for professor in r:
                professores.append(Professor.by_dict(professor))
        return [response, professores]

    def aluno(self, token: str, nome: str) -> list[requests.Response, list[Aluno]]:
        """Retorna umã lista de objetos do tipo Aluno.
        Return: list() [requests.Response, list() [Aluno]]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/aluno?nome={nome}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe Aluno.
        alunos = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for aluno in r:
                alunos.append(Aluno.by_dict(aluno))
        return [response, alunos]
