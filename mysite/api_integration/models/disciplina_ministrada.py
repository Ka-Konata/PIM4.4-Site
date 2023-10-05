from . professor import Professor
from . turma import Turma
from . disciplina import Disciplina

class Disciplina_Ministrada:
    """Model para a entidade Disciplina_Ministrada."""

    def __init__(self, 
                 id: int,
                 disciplina: Disciplina,
                 turma: Turma,
                 professor: Professor,
                 encerrada: bool,
                 coordenador: bool) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__disciplina = disciplina
        self.__turma = turma
        self.__professor = professor
        self.encerrada = encerrada
        self.coordenador = coordenador

    @property # retorna o valor encapsulado
    def id(self) -> int:
        return self.__id
    
    @property
    def disciplina(self) -> Disciplina:
        return self.__disciplina
    
    @property
    def turma(self) -> Turma:
        return self.__turma
    
    @property
    def professor(self) -> Professor:
        return self.professor
    
    @disciplina.setter # Altera o valor encapsulado
    def disciplina(self) -> None:
        pass # Ainda para implementar

    @turma.setter
    def turma(self) -> None:
        pass # Ainda para implementar

    @professor.setter
    def professor(self) -> None:
        pass # Ainda para implementar