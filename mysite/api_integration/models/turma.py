from . professor import Professor
from . aluno import Aluno
from . curso import Curso

class Turma:
    """Model para a entidade Turma."""

    def __init__(self, 
                 id: int,
                 nome: str,
                 curso: Curso,
                 alunos: list(Aluno),
                 professores: list(Professor),
                 coordenador: Professor) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__curso = curso
        self.__alunos = alunos
        self.__professores = professores
        self.nome = nome
        self.coordenador = coordenador

    @property # Retorna o valor encapsulado
    def id(self) -> int:
        return self.__id

    @property
    def curso(self) -> Curso:
        return self.__curso

    @property
    def alunos(self) -> list(Aluno):
        return self.__alunos

    @property
    def profesores(self) -> list(Professor):
        return self.__professores
    
    @curso.setter
    def curso(self) -> None:
        pass # Ainda para implementar
    
    @alunos.setter
    def alunos(self) -> None:
        pass # Ainda para implementar
    
    @profesores.setter
    def profesores(self) -> None:
        pass # Ainda para implementar