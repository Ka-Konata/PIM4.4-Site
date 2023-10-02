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
        self.__id = id
        self.__senha = senha
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__email = email
        self.__cargo = cargo
        """Construtor da classe."""

    def entrar(id: int, senha: str):
        pass # Ainda para implementar

    def get_id(self):
        return self.__id

    def get_senha(self):
        return self.__senha

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_cargo(self):
        return self.__cargo
    