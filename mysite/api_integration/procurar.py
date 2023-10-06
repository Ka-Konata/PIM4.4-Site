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

    def analistarh(self, id: int, token: str) -> list[requests.Response, AnalistaRH]:
        """Retorna um objeto AnalistaRH.
        Return: list() [requests.Response, AnalistaRH]"""
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
