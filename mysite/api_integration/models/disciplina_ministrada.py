from . professor import Professor
from . turma import Turma
from . disciplina import Disciplina
from api_integration.utils import get_value

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

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Disciplina_Ministrada(
            id=get_value(content, "id"),
            disciplina=Disciplina.by_dict(get_value(content, "disciplina")),
            turma=Turma.by_dict(get_value(content, "turma")),
            professor=Professor.by_dict(get_value(content, "professor")),
            encerrada=get_value(content, "encerrada"),
            coordenador=get_value(content, "coordenador")
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "id": self.id,
            "disciplina": self.disciplina.to_dict(),
            "turma": self.turma.to_dict(),
            "professor": self.professor.to_dict(),
            "encerrada": self.encerrada,
            "coordenador": self.coordenador
        }

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
        return self.__professor
    
    @disciplina.setter # Altera o valor encapsulado
    def disciplina(self) -> None:
        pass # Ainda para implementar

    @turma.setter
    def turma(self) -> None:
        pass # Ainda para implementar

    @professor.setter
    def professor(self) -> None:
        pass # Ainda para implementar