class Disciplina:
    """Model para a entidade Disciplina."""

    def __init__(self, 
                 id: int,
                 nome: str) -> None:
        """Construtor da classe."""
        self.__id = id
        self.nome = nome

    @property # retorna o valor encapsulado
    def id(self) -> int:
        return self.__id
