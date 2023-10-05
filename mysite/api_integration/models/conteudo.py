from . disciplina_ministrada import Disciplina_Ministrada
from api_integration.api import Connection

class Conteudo:
    """Model para a entidade Conteudo."""

    def __init__(self, 
                 id: int,
                 documento_url: str,
                 disciplina_ministrada: Disciplina_Ministrada) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__documento_url = documento_url
        self.__disciplina_ministrada = disciplina_ministrada

        @property # Retorna o valor encapsulado
        def id(self) -> int:
            return self.__id
        
        @property
        def documento_url(self) -> str:
            return self.__documento_url
        
        @property
        def disciplina_ministrada(self) -> Disciplina_Ministrada:
            return self.__disciplina_ministrada

        @disciplina_ministrada.setter # Modifica o valor encapsulado
        def alterar_disciplina_ministrada(self, conection: Connection, novo_id: int) -> None:
            pass # Ainda para implementar