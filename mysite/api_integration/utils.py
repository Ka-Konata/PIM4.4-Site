from requests import Response
from ast import literal_eval
from json import dumps

def get_value(content: dict, key: str):
    return content[key] if key in content.keys() else None

def bytes_to_dict(bytes: bytes):
    """Converte uma variável em bytes para dict."""
    return literal_eval(bytes.decode("UTF-8"))


def dict_to_josn(dict: dict) -> str:
    """Converte uma variável em dict para json (string)."""
    return dumps(dict, indent=4) #


def object_to_json(obj: object, tipo_de_objeto: str) -> str:
    """Converte um objeto para uma string json.
    \nNota: remove a marcação de atributo privado
    \nNota: remove a separação por underline, e aplica um capitalize()"""

    # Preparando para converter.
    dict_objeto = obj.__dict__
    novo_objeto = {}

    # Passando por cada key do dicionário.
    for c in range(0, len(dict_objeto)):
        # Removendo a marcação de atributo privado.
        keys = list(dict_objeto.keys())
        nova_key = keys[c].replace("_" + tipo_de_objeto + "__", "")

        # Removendo a separação por underline e aplicando o capitalize().
        key_dividida = nova_key.split("_")
        nova_key = key_dividida[0]
        if len(nova_key) > 1:
            for palavra in key_dividida[1:]:
                nova_key = nova_key + palavra.capitalize()

        novo_objeto[nova_key] = dict_objeto[keys[c]]
        
    # Convertentdo para json e retornando
    return dumps(novo_objeto)


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
