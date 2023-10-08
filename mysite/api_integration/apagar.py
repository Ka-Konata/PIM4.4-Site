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

    def __do_request(self, token: str, id: int, url: str, obj: object = None) -> requests.Response:
        # Preparando e efetuando o request na API.
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"

        if obj != None:
            url = self.base_url + f"/{url}"
            print(url)
            return requests.delete(url, headers=headers, data=dict_to_josn(obj.to_dict()))

        else:
            url = self.base_url + f"/{url}/{id}"
            return requests.delete(url, headers=headers)


    def analistarh(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo AnalistaRH.
        Return: list() [requests.Response, AnalistaRH]"""
        return self.__do_request(token, id, self.URLs.ANALISTARH)

    def secretario(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Secretario.
        Return: list() [requests.Response, Secretario]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.SECRETARIO)

    def professor(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Professor.
        Return: list() [requests.Response, Professor]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.PROFESSOR)

    def aluno(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Aluno.
        Return: list() [requests.Response, Aluno]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.ALUNO)

    def conteudo(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Conteudo.
        Return: list() [requests.Response, Conteudo]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CONTEUDO)

    def curso_matriculado(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Curso_Matriculado.
        Return: list() [requests.Response, Curso_Matriculado]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO_MATRICULADO)

    def curso(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Curso.
        Return: list() [requests.Response, Curso]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.CURSO)
    
    def disciplina_em_curso(self, token: str, id_curso: int, id_disciplina: int) -> requests.Response:
        """Em um cadastro do tipo Curso, é registrado uma discplina.
        param id_curso: int
        param id_disciplina: int
        Return: requests.Response"""
        data = self.Models.DISCIPLINA_EM_CURSO(id_curso, id_disciplina)
        return self.__do_request(token, None, self.URLs.DISCIPLINA_EM_CURSO, data)

    def disciplina_cursada(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Disciplina_Cursada.
        Return: list() [requests.Response, Disciplina_Cursada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_CURSADA)

    def disciplina_ministrada(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Disciplina_Ministrada.
        Return: list() [requests.Response, Disciplina_Ministrada]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA_MINISTRADA)

    def disciplina(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Disciplina.
        Return: list() [requests.Response, Disciplina]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.DISCIPLINA)

    def turma(self, token: str, id: int) -> list[requests.Response, object]:
        """Apaga um cadastro no banco de dados do tipo Turma.
        Return: list() [requests.Response, Turma]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, id, self.URLs.TURMA)
    
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
