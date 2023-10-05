from .pessoa import Pessoa

class Aluno(Pessoa):
    """Model para a entidade Aluno, herda Pessoa."""

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
        super().__init__(nome, cpf, rg, telefone, email, cargo, id, senha)
    