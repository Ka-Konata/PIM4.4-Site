import requests
import json
from . procurar import Procurar
from . consultar import Consultar
from . editar import Editar
from . apagar import Apagar
from . cadastrar import Cadastrar
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


class Connection:
    def __init__(self, base_url: str) -> None:
        """Classe para lidar com a integração da API, incluindo conexão, buscas, consultas e modificações."""
        self.__empty = None,
        self.__base_url = base_url
        self.__base_headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.__url_list = {
            "analistarh": "analistarh",
            "secretario": "secretario",
            "professor": "professor",
            "aluno": "aluno",
            "conteudo": "conteudo",
            "curso_matriculado": "cursoMatriculado",
            "curso": "curso",
            "disciplina_cursada": "disciplinaCursada",
            "disciplina_ministrada": "disciplinaMinistrada",
            "disciplina": "disciplina",
            "turma": "turma"
        }
        self.__classes_list = {
            "analistarh": AnalistaRH,
            "secretario": Secretario,
            "professor": Professor,
            "aluno": Aluno,
            "conteudo": Conteudo,
            "curso_matriculado": Curso_Matriculado,
            "curso": Curso,
            "disciplina_cursada": Disciplina_Cursada,
            "disciplina_ministrada": Disciplina_Ministrada,
            "disciplina": Disciplina,
            "turma": Turma
        }
        self.__procurar = Procurar(self.base_url, self.base_headers, self.__url_list, self.__classes_list)
        self.__consultar = Consultar(self.base_url, self.base_headers, self.__url_list, self.__classes_list)
        self.__editar = Editar(self.base_url, self.base_headers)
        self.__apagar = Apagar(self.base_url, self.base_headers)
        self.__cadastrar = Cadastrar(self.base_url, self.base_headers)

    def startup(self, u: AnalistaRH) -> requests.Response:
        """Cadastre a conta inicial do banco de dados\n
        Não funciona caso qualquer outra tabela do tipo pessoa já esteja cadastrada no banco de dados."""
        url = self.base_url + "/login/startup"
        data = {
            "nome": u.get_nome(),
            "cpf": u.get_cpf(),
            "rg": u.get_rg(),
            "email": u.get_email(),
            "telefone": u.get_telefone()
        }
        response = requests.post(url, dict_to_josn(data), headers=self.base_headers)
        return response

    def login(self, id: int, senha: str) -> requests.Response:
        """Pegue um token e um refresh_token referente a alguma conta."""
        url = self.base_url + f"/login?id={id}&senha={senha}"
        headers = {'Accept': '*/*'}
        response = requests.get(url,  headers=headers)
        return response

    def refresh(self, id: int, token: str, refresh_token: str):
        """Pegue um novo token através do refresh_token caso o mesmo ainda não esteja vencido."""
        url = self.base_url + "/login/refresh"
        data = {
            "token": token,
            "refreshToken": refresh_token,
            "id": id
        }
        response = requests.post(url, dict_to_josn(data), headers=self.base_headers)
        return response

    def mudar_senha(self, id: int, senha_antiga: str, senha_nova: str):
        """Mude a senha de uma conta, enviando apenas o id e as senhas novas e velhas."""
        url = self.base_url + "/login/mudarsenha"
        data = {
            "id": id,
            "senhaAntiga": senha_antiga,
            "senhaNova": senha_nova
        }
        response = requests.put(url, dict_to_josn(data), headers=self.base_headers)
        return response
    
    @property # Retorna o valor encapsulado
    def base_url(self) -> str:
        return self.__base_url
    
    @property
    def base_headers(self) -> dict:
        return self.__base_headers
    
    @property
    def consultar(self) -> Consultar:
        return self.__consultar
    
    @property
    def procurar(self) -> Procurar:
        return self.__procurar
    
    @property
    def editar(self) -> Editar:
        return self.__editar
    
    @property
    def apagar(self) -> Apagar:
        return self.__apagar
    
    @property
    def cadastrar(self) -> Cadastrar:
        return self.__cadastrar
