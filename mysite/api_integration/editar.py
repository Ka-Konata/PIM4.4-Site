import requests
from . utils import *

class Editar:
    """Classe para realizar edições na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, id: int, url: str, obj: object = None) -> requests.Response:
        # Preparando e efetuando o request na API.
        url = self.base_url + f"/{url}/{id}"
        headers = self.base_headers
        headers["Authorization"] = f"Bearer {token}"

        if obj != None:
            return requests.put(url, headers=headers, data=dict_to_josn(obj.to_dict()))
        else:
            return requests.put(url, headers=headers)

    def analistarh(self, token: str, id: int, analistarh: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo AnalistaRH.
        param analistarh: api.AnalistaRH
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.ANALISTARH, analistarh)

    def secretario(self, token: str, id: int, secretario: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Secretario.
        param secretario: api.Secretario
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.SECRETARIO, secretario)

    def professor(self, token: str, id: int, professor: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Professor.
        param professor: api.Professor
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.PROFESSOR, professor)

    def aluno(self, token: str, id: int, aluno: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Aluno.
        param aluno: api.Aluno
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.ALUNO, aluno)

    def conteudo(self, token: str, id: int, conteudo: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Conteudo.
        param conteudo: api.Conteudo
        Return: requests.Response"""
        # O conteúdo é o único que envia um body no dormato "multipart/form-data" e cin um arquivo. Portanto, o código para exutar o request precisa ser diferente do restante.
        url = self.base_url + f"/{self.URLs.CONTEUDO}"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"idDisciplinaMinistrada": conteudo.disciplina_ministrada.id}
        files=[('documento', (conteudo.documento.name, conteudo.documento, conteudo.documento.content_type))]
        return requests.put(url, headers=headers, data=data, files=files)

    def curso_matriculado(self, token: str, id: int, curso_matriculado: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Curso_Matriculado.
        param curso_matriculado: api.Curso_Matriculado
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.CURSO_MATRICULADO, curso_matriculado)

    def curso(self, token: str, id: int, curso: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Curso.
        param curso: api.Curso
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.CURSO, curso)

    def disciplina_cursada(self, token: str, id: int, disciplina_cursada: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Disciplina_Cursada.
        param disciplina_cursada: api.Disciplina_Cursada
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.DISCIPLINA_CURSADA, disciplina_cursada)

    def calcular_media(self, token: str, id_disciplina_ministrada: int) -> requests.Response:
        """Pede para a API calcular a média em um cadastro do tipo Disciplina_Cursada.
        Return: requests.Response"""
        return self.__do_request(token, id_disciplina_ministrada, self.URLs.CALCULAR_MEDIA)

    def calcular_frequencia(self, token: str, id_disciplina_ministrada: int) -> requests.Response:
        """Pede para a API calcular a frequência em um cadastro do tipo Disciplina_Cursada.
        Return: requests.Response"""
        return self.__do_request(token, id_disciplina_ministrada, self.URLs.CALCULAR_FREQUENCIA)

    def calcular_situacao(self, token: str, id_disciplina_ministrada: int) -> requests.Response:
        """Pede para a API calcular a situação em um cadastro do tipo Disciplina_Cursada.
        Return: requests.Response"""
        return self.__do_request(token, id_disciplina_ministrada, self.URLs.CALCULAR_SITUACAO)

    def disciplina_ministrada(self, token: str, id: int, disciplina_ministrada: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Disciplina_Ministrada.
        param disciplina_ministrada: api.Disciplina_Ministrada
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.DISCIPLINA_MINISTRADA, disciplina_ministrada)

    def disciplina(self, token: str, id: int, disciplina: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Disciplina.
        param disciplina: api.Disciplina
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.DISCIPLINA, disciplina)

    def turma(self, token: str, id: int, turma: object) -> requests.Response:
        """Altera um cadastro já inserido no banco de dados. Cadastro do tipo Turma.
        param turma: api.Turma
        Return: requests.Response"""
        return self.__do_request(token, id, self.URLs.TURMA, turma)
    
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
