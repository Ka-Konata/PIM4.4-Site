class B:
    def __init__(self, arg: str) -> None:
        self.__quatrocentos_um = 1234

class A:
    def __init__(self, arg: str) -> None:
        self.__um_dois_tres_quatro = 1234
        self.idade_agr = 10
        self.nome = "nome"
        self.__arg = arg

    @property
    def arg(self):
        return self.__arg
    
    @arg.setter
    def arg(self, novo_arg):
        self.__arg = novo_arg
    
    def hello(self):
        print(self.arg)

    def class_name(self):
        print(self.__class__.__name__)

def object_to_json(obj: object, classe) -> str:
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
        nova_key = keys[c].replace("_" + classe + "__", "")

        # Removendo a separação por underline e aplicando o capitalize().
        key_dividida = nova_key.split("_")
        nova_key = key_dividida[0]
        if len(nova_key) > 1:
            for palavra in key_dividida[1:]:
                nova_key = nova_key + palavra.capitalize()

        novo_valor = dict_objeto[keys[c]]
        #if novo_valor.

        novo_objeto[nova_key] = dict_objeto[keys[c]]
        
    # Convertentdo para json e retornando
    return json.dumps(novo_objeto)

import json
a = A("Hello World")
a.class_name()
print(object_to_json(a, a.__class__.__name__))

def b(obj, classe):
    if isinstance("a", object):
        print(True)
    else:
        print(False)

b(a, A)
b(a, B)