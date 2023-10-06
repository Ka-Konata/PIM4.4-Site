from api_integration.utils import get_value

class Pessoa:
    """Model para a entidade herda Pessoa."""
    def __init__(self, 
                 nome: str, 
                 cpf: int, 
                 rg: int, 
                 telefone: int, 
                 email: str = None,
                 cargo: str = None,
                 id: int = None,  
                 senha: str = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__senha = senha
        self.__cargo = cargo
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.email = email

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Pessoa(
            id = get_value(content, "id"),
            senha = get_value(content, "senha"),
            cargo = get_value(content, "cargo"),
            nome = get_value(content, "nome"),
            cpf = get_value(content, "cpf"),
            rg = get_value(content, "rg"),
            telefone = get_value(content, "telefone"),
            email = get_value(content, "email")
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "id": self.id,
            "senha": self.senha,
            "cargo": self.cargo,
            "nome": self.nome,
            "cpf": self.cpf,
            "rg": self.rg,
            "telefone": self.telefone,
            "email": self.email
        }

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id

    @property
    def senha(self) -> str:
        return self.__senha

    @property
    def cargo(self) -> str:
        return self.__cargo

    