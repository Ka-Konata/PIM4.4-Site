from requests import Response
from ast import literal_eval
from json import dumps

def get_value(content: dict, key: str):
    if content != None:
        return content[key] if key in content.keys() else None
    else:
        return None

def bytes_to_dict(bytes: bytes):
    """Converte uma variável em bytes para dict."""
    bytes = bytes.decode("UTF-8")
    bytes = bytes.replace("null", "None")
    bytes = bytes.replace("true", "True")
    bytes = bytes.replace("false", "False")
    return literal_eval(bytes)


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

def get_file_path(documento_url: str) -> str:
    r = documento_url.replace("/api/file/conteudo/", "")
    r = r.replace("/api/file/certificado/", "")
    return  r


class Login:
    def __init__(
            self, 
            token: str = None, 
            refresh_token: str = None, 
            cargo: str = None, 
            id: int = None,
            email: str = None,
            valido: bool = None 
            ) -> None:
        """Uma classe para guardar algumas informações básicas de login."""
        self.token = token
        self.refresh_token = refresh_token
        self.cargo = cargo
        self.id = id
        self.email = email
        self.valido = valido

    def set_values_with_response(self, r: Response) -> None:
        """Uma função que pega as informações de uma objeto requests.Response e insere no objeto atual."""
        res = bytes_to_dict(r.content)
        self.token = get_value(res, "token")
        self.refresh_token = get_value(res, "refreshToken")
        self.cargo = get_value(res, "cargo")
        self.id = get_value(res, "id")
        self.email = get_value(res, "email")

    def set_refresh(self, r: Response) -> None:
        """Atualiza as informações do objeto atual ao fazer o refresh to token."""
        res = bytes_to_dict(r.content)
        self.token = get_value(res, "token")
        self.valido = get_value(res, "valido")
        


class Cargo:
    ANALISTARH = "AnalistaRH"
    SECRETARIO = "Secretario"
    PROFESSOR = "Professor"
    ALUNO = "Aluno"
    TODOS = [ANALISTARH, SECRETARIO, PROFESSOR, ALUNO]
