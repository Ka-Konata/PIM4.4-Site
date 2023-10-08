import requests
from . utils import *

class Consultar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, id: int, url: str, model: any) -> list[requests.Response, any]:
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/{url}/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe.
        obj = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            obj = model.by_dict(r)
        return [response, obj]


    def analistarh(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo AnalistaRH.
        Return: list() [requests.Response, AnalistaRH]"""
        return self.__do_request(token, id, self.URLs.ANALISTARH, self.Models.ANALISTARH)

    def secretario(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Secretario.
        Return: list() [requests.Response, Secretario]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.SECRETARIO, self.Models.SECRETARIO)

    def professor(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Professor.
        Return: list() [requests.Response, Professor]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.PROFESSOR, self.Models.PROFESSOR)

    def aluno(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Aluno.
        Return: list() [requests.Response, Aluno]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.ALUNO, self.Models.ALUNO)

    def conteudo(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Conteudo.
        Return: list() [requests.Response, Conteudo]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CONTEUDO, self.Models.CONTEUDO)

    def curso_matriculado(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Curso_Matriculado.
        Return: list() [requests.Response, Curso_Matriculado]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO_MATRICULADO, self.Models.CURSO_MATRICULADO)

    def curso(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Curso.
        Return: list() [requests.Response, Curso]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO, self.Models.CURSO)

    def disciplina_cursada(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Disciplina_Cursada.
        Return: list() [requests.Response, Disciplina_Cursada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_CURSADA, self.Models.DISCIPLINA_CURSADA)

    def disciplina_ministrada(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Disciplina_Ministrada.
        Return: list() [requests.Response, Disciplina_Ministrada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_MINISTRADA, self.Models.DISCIPLINA_MINISTRADA)

    def disciplina(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Disciplina.
        Return: list() [requests.Response, Disciplina]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA, self.Models.DISCIPLINA)

    def turma(self, token: str, id: int) -> list[requests.Response, object]:
        """Com um id específico, busca um cadastro no banco de dados do tipo Turma.
        Return: list() [requests.Response, Turma]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.TURMA, self.Models.TURMA)

    @property
    def URLs(self):
        return self.__URLs
    
    @property
    def Models(self):
        return self.__Models
