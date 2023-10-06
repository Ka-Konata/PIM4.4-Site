from . disciplina_ministrada import Disciplina_Ministrada
from .. import api
from api_integration.utils import get_value

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

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Conteudo(
            id=get_value(content, "id"),
            documento_url=get_value(content, "documentoURL"),
            disciplina_ministrada=Disciplina_Ministrada.by_dict(get_value(content, "disciplinaMinistrada"))
        )

    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "id": self.id,
            "documento_url": self.documento_url,
            "disciplina_ministrada": self.disciplina_ministrada
        }

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
    def disciplina_ministrada(self, conection: any, novo_id: int) -> None:
        pass # Ainda para implementar