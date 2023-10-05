from . disciplina import Disciplina

class Curso:
    """Model para a entidade Curso."""

    def __init__(self, 
                 id: int,
                 nome: str,
                 carga_horaria: int,
                 aulas_totais: int,
                 disciplinas: list(Disciplina)) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__disciplinas = disciplinas
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_totais = aulas_totais

        @property # Retorna o valor encapsulado
        def id(self) -> int:
            return self.__id
        
        @property
        def disciplinas(self) -> list(Disciplina):
            return self.__disciplinas
        
        @disciplinas.setter # Altera o valor encapsulado
        def disciplinas(self) -> None:
            pass # Ainda para implementar
