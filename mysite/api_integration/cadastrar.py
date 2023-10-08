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
        return requests.post(url, headers=headers, data=dict_to_josn(obj.to_dict()))

    def analistarh(self, token: str, analistarh: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo AnalistaRH.
        param analistarh: api.AnalistaRH
        Return: requests.Response"""
        return self.__do_request(token, analistarh, self.URLs.ANALISTARH)

    def secretario(self, token: str, secretario: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Secretario.
        param secretario: api.Secretario
        Return: requests.Response"""
        return self.__do_request(token, secretario, self.URLs.SECRETARIO)

    def professor(self, token: str, professor: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Professor.
        param professor: api.Professor
        Return: requests.Response"""
        return self.__do_request(token, professor, self.URLs.PROFESSOR)

    def aluno(self, token: str, aluno: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Aluno.
        param aluno: api.Aluno
        Return: requests.Response"""
        return self.__do_request(token, aluno, self.URLs.ALUNO)

    def conteudo(self, token: str, conteudo: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Conteudo.
        param conteudo: api.Conteudo
        Return: requests.Response"""
        # O conteúdo é o único que envia um body no dormato "multipart/form-data" e cin um arquivo. Portanto, o código para exutar o request precisa ser diferente do restante.
        url = self.base_url + f"/{self.URLs.CONTEUDO}"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"idDisciplinaMinistrada": conteudo.disciplina_ministrada.id}
        files=[('documento', (conteudo.documento.name, conteudo.documento, conteudo.documento.content_type))]
        return requests.post(url, headers=headers, data=data, files=files)

    def curso_matriculado(self, token: str, curso_matriculado: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Curso_Matriculado.
        param curso_matriculado: api.Curso_Matriculado
        Return: requests.Response"""
        return self.__do_request(token, curso_matriculado, self.URLs.CURSO_MATRICULADO)

    def disciplina_cursada(self, token: str, disciplina_cursada: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Disciplina_Cursada.
        param disciplina_cursada: api.Disciplina_Cursada
        Return: requests.Response"""
        return self.__do_request(token, disciplina_cursada, self.URLs.DISCIPLINA_CURSADA)

    def disciplina_ministrada(self, token: str, disciplina_ministrada: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Disciplina_Ministrada.
        param disciplina_ministrada: api.Disciplina_Ministrada
        Return: requests.Response"""
        return self.__do_request(token, disciplina_ministrada, self.URLs.DISCIPLINA_MINISTRADA)

    def disciplina(self, token: str, disciplina: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Disciplina.
        param disciplina: api.Disciplina
        Return: requests.Response"""
        return self.__do_request(token, disciplina, self.URLs.DISCIPLINA)

    def turma(self, token: str, turma: object) -> requests.Response:
        """Realiza um novo cadastro no banco de dados do tipo Turma.
        param turma: api.Turma
        Return: requests.Response"""
        return self.__do_request(token, turma, self.URLs.TURMA)
    
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
