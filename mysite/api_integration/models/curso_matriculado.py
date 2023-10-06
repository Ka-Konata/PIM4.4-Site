from . disciplina import Disciplina
from . aluno import Aluno
from . curso import Curso
from . turma import Turma
from api_integration.utils import get_value

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
                disciplinas: list[Disciplina]) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__aluno = aluno
        self.__curso = curso
        self.__turma = turma
        self.__disciplinas = disciplinas
        self.semestre_atual = semestre_atual
        self.trancado = trancado
        self.finalizado = finalizado

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        # Instanciando cada disciplina para o objeto.
        disciplinas = []
        for d in get_value(content, "disciplinas"):
            disciplinas.append(Disciplina.by_dict(d))

        return Curso_Matriculado(
            id=get_value(content, "id"),
            aluno=Aluno.by_dict(get_value(content, "aluno")),
            curso=Curso.by_dict(get_value(content, "curso")),
            turma=Turma.by_dict(get_value(content, "turma")),
            semestre_atual=get_value(content, "semestreAtual"),
            trancado=get_value(content, "trancado"),
            finalizado=get_value(content, "finalizado"),
            disciplinas=disciplinas
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        # Previamente é necessário converter cada disciplina, aluno, curso e turma em discionarios também.
        disciplinas = []
        for d in self.disciplinas:
            disciplinas.append(d.to_dict())

        return {
            "id": self.id,
            "aluno": self.aluno.to_dict(),
            "curso": self.curso.to_dict(),
            "turma": self.turma.to_dict(),
            "semestre_atual": self.semestre_atual,
            "trancado": self.trancado,
            "finalizado": self.finalizado,
            "disciplinas": disciplinas
        }

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
    def disciplinas(self) -> list[Disciplina]:
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
