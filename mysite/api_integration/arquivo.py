import requests
from . utils import *

class Arquivo:
    """Classe para pegar arquivos na API."""
    def __init__(self, base_url: str, base_headers: dict, urls, models) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers
        self.__URLs = urls
        self.__Models = models

    def __do_request(self, token: str, path: str, url: str) -> list[requests.Response, any]:
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/{url}/{path}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        
        return requests.get(url, headers=headers)

    def conteudo(self, token: str, path: int) -> requests.Response:
        """Busca por um arquivo do tipo conteudo.
        Return: requests.Response"""
        return self.__do_request(token, path, self.URLs.FILE_CONTEUDO)

    def boletim(self, token: str, path: int) -> requests.Response:
        """Busca por um arquivo do tipo boletim.
        Return: requests.Response"""
        return self.__do_request(token, path, self.URLs.FILE_BOLETIM)

    def historico(self, token: str, path: int) -> requests.Response:
        """Busca por um arquivo do tipo historico.
        Return: requests.Response"""
        return self.__do_request(token, path, self.URLs.FILE_HISTORICO)

    def declaracao(self, token: str, path: int) -> requests.Response:
        """Busca por um arquivo do tipo declaracao.
        Return: requests.Response"""
        return self.__do_request(token, path, self.URLs.FILE_DECLARACAO)

    def relatorio(self, token: str, path: int) -> requests.Response:
        """Busca por um arquivo do tipo relatorio.
        Return: requests.Response"""
        return self.__do_request(token, path, self.URLs.FILE_RELATORIO)

    @property
    def URLs(self):
        return self.__URLs
    
    @property
    def Models(self):
        return self.__Models
