import requests
import json
from . procurar import Procurar
from . consultar import Consultar
from . models.analistarh import AnalistaRH
from . utils import *


class Connection:
    def __init__(self, base_url: str) -> None:
        """Classe para lidar com a integração da API, incluindo conexão, buscas, consultas e modificações."""
        self.__empty = None,
        self.__base_url = base_url
        self.__base_headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.procurar = Procurar(self.__base_url, self.__base_headers)
        self.consultar = Consultar(self.__base_url, self.__base_headers)

    def startup(self, u: AnalistaRH) -> requests.Response:
        """Cadastre a conta inicial do banco de dados\n
        Não funciona caso qualquer outra tabela do tipo pessoa já esteja cadastrada no banco de dados."""
        url = self.__base_url + "/login/startup"
        data = {
            "nome": u.get_nome(),
            "cpf": u.get_cpf(),
            "rg": u.get_rg(),
            "email": u.get_email(),
            "telefone": u.get_telefone()
        }
        response = requests.post(url, dict_to_josn(data), headers=self.__base_headers)
        return response

    def login(self, id: int, senha: str) -> requests.Response:
        """Pegue um token e um refresh_token referente a alguma conta."""
        url = self.__base_url + f"/login?id={id}&senha={senha}"
        headers = {'Accept': '*/*'}
        response = requests.get(url,  headers=headers)
        return response

    def refresh(self, id: int, token: str, refresh_token: str):
        """Pegue um novo token através do refresh_token caso o mesmo ainda não esteja vencido."""
        url = self.__base_url + "/login/refresh"
        data = {
            "token": token,
            "refreshToken": refresh_token,
            "id": id
        }
        response = requests.post(url, dict_to_josn(data), headers=self.__base_headers)
        return response

    def mudar_senha(self, id: int, senha_antiga: str, senha_nova: str):
        """Mude a senha de uma conta, enviando apenas o id e as senhas novas e velhas."""
        url = self.__base_url + "/login/mudarsenha"
        data = {
            "id": id,
            "senhaAntiga": senha_antiga,
            "senhaNova": senha_nova
        }
        response = requests.put(url, dict_to_josn(data), headers=self.__base_headers)
        return response
    