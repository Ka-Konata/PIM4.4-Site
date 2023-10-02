from requests import Response
from ast import literal_eval
from json import dumps

def bytes_to_dict(bytes: bytes):
    """Converte uma variável em bytes para dict."""
    return literal_eval(bytes.decode("UTF-8"))


def dict_to_josn(dict: dict) -> str:
    """Converte uma variável em dict para json (string)."""
    return dumps(dict, indent=4) #


class Login:
    def __init__(self, r: Response) -> None:
        """Uma classe para guardar algumas informações básicas de login."""
        res = bytes_to_dict(r.content)
        self.token = res["token"]
        self.refresh_token = res["refreshToken"]
        self.cargo = res["cargo"]
        self.id = res["id"]
        self.email = res["email"]