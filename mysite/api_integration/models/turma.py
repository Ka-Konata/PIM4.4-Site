from . professor import Professor
from . aluno import Aluno
from . curso import Curso
from api_integration.utils import get_value

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

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        # Instanciando cada aluno e professor para o objeto.
        alunos = []
        for a in get_value(content, "alunos"):
            alunos.append(Aluno.by_dict(a))

        professores = []
        for p in get_value(content, "professores"):
            professores.append(Professor.by_dict(p))

        return Turma(
            id=get_value(content, "id"),
            nome=get_value(content, "nome"),
            curso=Curso.by_dict(get_value(content, "curso")),
            alunos=alunos,
            professores=professores,
            coordenador=Professor(get_value(content, "coordenador"))
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        # Previamente é necessário converter cada disciplina, aluno, curso e turma em discionarios também.
        alunos = []
        for a in self.alunos:
            alunos.append(a.to_dict())
            
        professores = []
        for p in self.alunos:
            professores.append(p.to_dict())

        return {
            "id": self.id,
            "nome": self.nome,
            "curso": self.curso.to_dict(),
            "alunos": alunos,
            "professores": professores,
            "coordenador": self.coordenador.to_dict()
        }

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