import requests
import json
from ast import literal_eval
from procurar import Procurar
from models.analistarh import AnalistaRH


def bytes_to_dict(bytes: bytes):
    """Converte uma variável em bytes para dict."""
    return literal_eval(bytes.decode("UTF-8"))


def dict_to_josn(dict: dict) -> str:
    """Converte uma variável em dict para json (string)."""
    return json.dumps(dict, indent=4) #


class Login:
    def __init__(self, r: requests.Response) -> None:
        """Uma classe para guardar algumas informações básicas de login."""
        res = bytes_to_dict(r.content)
        self.token = res["token"]
        self.refresh_token = res["refreshToken"]
        self.cargo = res["cargo"]
        self.id = res["id"]
        self.email = res["email"]


class Connection:
    def __init__(self, base_url: str) -> None:
        """Classe para lidar com a integração da API, incluindo conexão, buscas, consultas e modificações."""
        self.__empty = None,
        self.__base_url = base_url
        self.__base_headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        self.procurar = Procurar(self.__base_url)

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
    