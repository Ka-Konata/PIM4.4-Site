class Pessoa:
    """Model para a entidade herda Pessoa."""

    def __init__(self, 
                 nome: str, 
                 cpf: int, 
                 rg: int, 
                 telefone: int, 
                 email: str,
                 cargo: str = None,
                 id: int = None,  
                 senha: str = None
                 ) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__senha = senha
        self.__cargo = cargo
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.email = email

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id

    @property
    def senha(self) -> str:
        return self.__senha

    @property
    def cargo(self) -> str:
        return self.__cargo

    