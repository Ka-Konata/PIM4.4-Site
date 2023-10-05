from . disciplina import Disciplina
from . aluno import Aluno
from . curso import Curso
from . turma import Turma

class Curso_Matriculado:
    """Model para a entidade Curso_Matriculado."""

    def __init__(self, 
                id: int,
                aluno: Aluno,
                curso: Curso,
                turma: Turma,
                semestre_atual: int,
                trancado: bool,
                finalizado: bool,
                disciplinas: list(Disciplina)) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__aluno = aluno
        self.__curso = curso
        self.__turma = turma
        self.__disciplinas = disciplinas
        self.semestre_atual = semestre_atual
        self.trancado = trancado
        self.finalizado = finalizado

        @property # Retorna o valor encapsulado
        def id(self) -> int:
            return self.__id
        
        @property
        def aluno(self) -> Aluno:
            return self.__aluno
        
        @property
        def turma(self) -> Turma:
            return self.__turma
        
        @property
        def curso(self) -> Curso:
            return self.__curso
        
        @property
        def disciplinas(self) -> list(Disciplina):
            return self.__disciplinas
        
        @aluno.setter # Altera o valor encapsulado
        def aluno(self) -> None:
            pass # Ainda para implementar
        
        @turma.setter
        def turma(self) -> None:
            pass # Ainda para implementar
        
        @curso.setter
        def curso(self) -> None:
            pass # Ainda para implementar
        
        @disciplinas.setter
        def disciplinas(self) -> None:
            pass # Ainda para implementar
