from . disciplina import Disciplina
from . curso_matriculado import Curso_Matriculado
from api_integration.utils import get_value

class Disciplina_Cursada:
    """Model para a entidade Disciplina_Cursada."""

    def __init__(self, 
                 disciplina: Disciplina,
                 curso_matriculado: Curso_Matriculado,
                 prova1: float,
                 prova2: float,
                 trabalho: float,
                 faltas: int,
                 id: int = None,
                 media: float = None,
                 frequencia: int = None,
                 situacao: str = None) -> None:
        """Construtor da classe."""
        self.__id = id
        self.__disciplina = disciplina
        self.__curso_matriculado = curso_matriculado
        self.__media = media
        self.__frequencia = frequencia
        self.__situacao = situacao
        self.prova1 = prova1
        self.prova2 = prova2
        self.trabalho = trabalho
        self.faltas = faltas

    def by_dict(content: dict) -> object:
        """Instancia a classe a partir de um dicionário."""
        return Disciplina_Cursada(
            id=get_value(content, "id"),
            disciplina=Disciplina.by_dict(get_value(content, "disciplina")),
            curso_matriculado=Curso_Matriculado.by_dict(get_value(content, "cursoMatriculado")),
            prova1=get_value(content, "prova1"),
            prova2=get_value(content, "prova2"),
            trabalho=get_value(content, "trabalho"),
            media=get_value(content, "media"),
            faltas=get_value(content, "faltas"),
            frequencia=get_value(content, "frequencia"),
            situacao=get_value(content, "situacao")
        )
    
    def to_dict(self) -> dict:
        """Converte o objeto atual em um discionário."""
        return {
            "idDisciplina": self.disciplina.id,
            "idCursoMatriculado": self.curso_matriculado.id,
            "prova1": self.prova1,
            "prova2": self.prova2,
            "trabalho": self.trabalho,
            "faltas": self.faltas,
        }
    
    def to_context(self) -> dict:
        """Converte o objeto atual em um discionário para inserir em um context."""
        return {
            "id": self.id,
            "disciplina": self.disciplina.to_dict(),
            "curso_matriculado": self.curso_matriculado.to_dict(),
            "prova1": self.prova1,
            "prova2": self.prova2,
            "trabalho": self.trabalho,
            "media": self.media,
            "faltas": self.faltas,
            "frequencia": self.frequencia,
            "situacao": self.situacao
        }

    @property # retorna o valor encapsulado
    def id(self) -> int:
        return self.__id
    
    @property
    def curso_matriculado(self) -> Curso_Matriculado:
        return self.__curso_matriculado
    
    @property
    def disciplina(self) -> Disciplina:
        return self.__disciplina
    
    @property
    def media(self) -> float:
        return self.__media
    
    @property
    def frequencia(self) -> int:
        return self.__frequencia
    
    @property
    def situacao(self) -> str:
        return self.__situacao
    
    @disciplina.setter # Altera o valor encapsulado
    def disciplina(self) -> None:
        pass # Ainda para implementar
    
    @curso_matriculado.setter # Altera o valor encapsulado
    def curso_matriculado(self) -> None:
        pass # Ainda para implementar
    
    @media.setter
    def media(self) -> None:
        pass # Ainda para implementar
    
    @frequencia.setter
    def frequencia(self) -> None:
        pass # Ainda para implementar
    
    @situacao.setter
    def situacao(self) -> None:
        pass # Ainda para implementar
