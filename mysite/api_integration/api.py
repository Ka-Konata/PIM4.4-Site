import requests
import json
from . procurar import Procurar
from . consultar import Consultar
from . editar import Editar
from . apagar import Apagar
from . cadastrar import Cadastrar
from . utils import *
from . models.pessoa import Pessoa
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


class Connection:
    def __init__(self, base_url: str) -> None:
        """Classe para lidar com a integração da API, incluindo conexão, buscas, consultas e modificações."""
        self.__empty = None,
        self.__base_url = base_url
        self.__base_headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        self.__procurar = Procurar(self.base_url, self.base_headers, URLs, Models)
        self.__consultar = Consultar(self.base_url, self.base_headers, URLs, Models)
        self.__editar = Editar(self.base_url, self.base_headers, URLs, Models)
        self.__apagar = Apagar(self.base_url, self.base_headers, URLs, Models)
        self.__cadastrar = Cadastrar(self.base_url, self.base_headers, URLs, Models)

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
        return requests.post(url, dict_to_josn(data), headers=self.base_headers)

    def login(self, id: int, senha: str) -> requests.Response:
        """Pegue um token e um refresh_token referente a alguma conta."""
        url = self.base_url + f"/login?id={id}&senha={senha}"
        headers = {'Accept': '*/*'}
        return requests.get(url,  headers=headers)

    def refresh(self, id: int, token: str, refresh_token: str):
        """Pegue um novo token através do refresh_token caso o mesmo ainda não esteja vencido."""
        url = self.base_url + "/login/refresh"
        data = {
            "token": token,
            "refreshToken": refresh_token,
            "id": id
        }
        return requests.post(url, dict_to_josn(data), headers=self.base_headers)

    def mudar_senha(self, id: int, senha_antiga: str, senha_nova: str):
        """Mude a senha de uma conta, enviando apenas o id e as senhas novas e velhas."""
        url = self.base_url + "/login/mudarsenha"
        data = {
            "id": id,
            "senhaAntiga": senha_antiga,
            "senhaNova": senha_nova
        }
        return requests.put(url, dict_to_josn(data), headers=self.base_headers)
    
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


class URLs:
    ANALISTARH = "analistarh"
    SECRETARIO = "secretario"
    PROFESSOR = "professor"
    ALUNO = "aluno"
    CONTEUDO = "conteudo"
    CURSO_MATRICULADO = "cursoMatriculado"
    CURSO = "curso"
    DISCIPLINA_EM_CURSO = "curso/disciplina"
    DISCIPLINA_CURSADA = "disciplinaCursada"
    DISCIPLINA_MINISTRADA = "disciplinaMinistrada"
    DISCIPLINA = "disciplina"
    TURMA = "turma"


class Models:
    PESSOA = Pessoa
    ANALISTARH = AnalistaRH
    SECRETARIO = Secretario
    PROFESSOR = Professor
    ALUNO = Aluno
    CONTEUDO = Conteudo
    CURSO_MATRICULADO = Curso_Matriculado
    CURSO = Curso
    DISCIPLINA_EM_CURSO = Curso.Disicplina_Em_Curso
    DISCIPLINA_CURSADA = Disciplina_Cursada
    DISCIPLINA_MINISTRADA = Disciplina_Ministrada
    DISCIPLINA = Disciplina
    TURMA = Turma
