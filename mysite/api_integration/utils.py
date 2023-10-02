from requests import Response
from ast import literal_eval
from json import dumps

def bytes_to_dict(bytes: bytes):
    """Converte uma variável em bytes para dict."""
    return literal_eval(bytes.decode("UTF-8"))


def dict_to_josn(dict: dict) -> str:
    """Converte uma variável em dict para json (string)."""
    return dumps(dict, indent=4) #


class Cargo:
    ANALISTARH = "AnalistaRH"
    SECRETARIO = "Secretario"
    PROFESSOR = "Professor"
    ALUNO = "Aluno"
    TODOS = [ANALISTARH, SECRETARIO, PROFESSOR, ALUNO]


class Login:
    def __init__(
            self, 
            token: str = None, 
            refresh_token: str = None, 
            cargo: str = None, 
            id: int = None,
            email: str = None
            ) -> None:
        """Uma classe para guardar algumas informações básicas de login."""
        self.token = token
        self.refresh_token = refresh_token
        self.cargo = cargo
        self.id = id
        self.email = email

    def set_values_with_response(self, r: Response) -> None:
        """Uma classe para guardar algumas informações básicas de login."""
        res = bytes_to_dict(r.content)
        self.token = res["token"]
        self.refresh_token = res["refreshToken"]
        self.cargo = res["cargo"]
        self.id = res["id"]
        self.email = res["email"]
