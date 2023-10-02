import requests
import json
from . models.analistarh import AnalistaRH
from . utils import *
from django.http import HttpResponse

class Consultar:
    """Classe para realizar pesquisas na API."""
    def __init__(self, base_url: str, base_headers: dict) -> None:
        """Construtor da classe."""
        self.__base_url = base_url
        self.__base_headers = base_headers

    def analistarh(self, id: int, token: str) -> list[HttpResponse, AnalistaRH]:
        """Retorna um objeto AnalistaRH.
        Return: list() [django.http.HttpResponse, AnalistaRH]"""
        # Preparando e efetuando o request na API.
        url = self.__base_url + f"/analistarh/{id}"
        headers = self.__base_headers
        headers["Authorization"] = f"Bearer {token}"
        response = requests.get(url, headers=headers)

        # Instanciando o objeto da classe AnalistaRH.
        analistarh = None
        if response.status_code == 200:
            r = bytes_to_dict(response.content)
            analistarh = AnalistaRH(
                id=r["id"],
                nome=r["nome"],
                cpf=r["cpf"],
                rg=r["rg"],
                telefone=r["telefone"],
                email=r["email"],
                cargo=r["cargo"]
            )
        return [response, analistarh]
