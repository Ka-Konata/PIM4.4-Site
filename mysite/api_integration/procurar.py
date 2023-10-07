import requests
from . utils import *

class Procurar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, url: str, model: any, filtro_nome: str = None, filtro_value = None) -> list[requests.Response, list[any]]:
        # Preparando e efetuando o request na API.
        url = self.base_url + f"/{url}"
        if filtro_nome != None and filtro_value != None:
            url = url + f"?{filtro_nome}={filtro_value}"
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe.
        objs = []
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            for obj in r:
                objs.append(model.by_dict(obj))
        return [response, objs]

    def analistarh(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo AnalistaRH.
        Return: list() [requests.Response, list() [AnalistaRH]]"""
        return self.__do_request(token, self.URLs.ANALISTARH, self.Models.ANALISTARH, "nome", nome)

    def secretario(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Secretario.
        Return: list() [requests.Response, list() [Secretario]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.SECRETARIO, self.Models.SECRETARIO, "nome", nome)

    def professor(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Professor.
        Return: list() [requests.Response, list() [Professor]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.PROFESSOR, self.Models.PROFESSOR, "nome", nome)

    def aluno(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Aluno.
        Return: list() [requests.Response, list() [Aluno]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.ALUNO, self.Models.ALUNO, "nome", nome)

    def conteudo(self, token: str, id_disciplina_ministrada: int = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Conteudo.
        Return: list() [requests.Response, list() [Conteudo]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.CONTEUDO, self.Models.CONTEUDO, "idDisciplinaMinistrada", id_disciplina_ministrada)

    def curso_matriculado(self, token: str, id_aluno: int = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Curso_Matriculado.
        Return: list() [requests.Response, list() [Curso_Matriculado]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.CURSO_MATRICULADO, self.Models.CURSO_MATRICULADO, "idAluno", id_aluno)

    def curso(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Curso.
        Return: list() [requests.Response, list() [Curso]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.CURSO, self.Models.CURSO, "nome", nome)

    def disciplina_cursada(self, token: str, id_professor: int = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Disciplina_Cursada.
        Return: list() [requests.Response, list() [Disciplina_Cursada]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.DISCIPLINA_CURSADA, self.Models.DISCIPLINA_CURSADA, "idProfessor", id_professor)

    def disciplina_ministrada(self, token: str, id_curso_matriculado: int = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Disciplina_Ministrada.
        Return: list() [requests.Response, list() [Disciplina_Ministrada]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.DISCIPLINA_MINISTRADA, self.Models.DISCIPLINA_MINISTRADA, "idCursoMatriculado", id_curso_matriculado)

    def disciplina(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Disciplina.
        Return: list() [requests.Response, list() [Disciplina]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.DISCIPLINA, self.Models.DISCIPLINA, "nome", nome)

    def turma(self, token: str, nome: str = None) -> list[requests.Response, list]:
        """Retorna umã lista de objetos do tipo Turma.
        Return: list() [requests.Response, list() [Turma]]"""
        # Preparando e efetuando o request na API.
        return self.__do_request(token, self.URLs.TURMA, self.Models.TURMA, "nome", nome)
    
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
