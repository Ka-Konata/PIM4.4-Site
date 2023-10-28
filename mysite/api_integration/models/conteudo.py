from . disciplina_ministrada import Disciplina_Ministrada
from .. import api
from api_integration.utils import get_value

class Conteudo:
    """Model para a entidade Conteudo."""

    def __init__(self, 
                 disciplina_ministrada: Disciplina_Ministrada,
                 id: int = None,
                 documento_url: str = None,
                 documento = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__documento_url = documento_url
        self.__disciplina_ministrada = disciplina_ministrada
        self.__documento = documento

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Conteudo(
            id=get_value(content, "id"),
            documento_url=get_value(content, "documentoURL"),
            disciplina_ministrada=Disciplina_Ministrada.by_dict(get_value(content, "disciplinaMinistrada")),
            documento=get_value(content, "documento")
        )

    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "idDisciplinaMinistrada": self.disciplina_ministrada,
            "documento": self.documento
        }

    def to_context(self) -> dict:
        """Converte o objeto atual em um discionário para inserir em um context."""
        return {
            "id": self.id,
            "documentoURL": self.documento_url,
            "disciplina_ministrada": self.disciplina_ministrada
        }

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id

    @property
    def documento_url(self) -> str:
        return self.__documento_url
    
    @documento_url.setter
    def documento_url(self, value) -> None:
        self.__documento_url = value

    @property
    def disciplina_ministrada(self) -> Disciplina_Ministrada:
        return self.__disciplina_ministrada
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, value) -> None:
        self.__documento = value