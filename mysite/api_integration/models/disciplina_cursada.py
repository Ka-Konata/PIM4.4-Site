from . disciplina import Disciplina
from . curso_matriculado import Curso_Matriculado

class Disciplina_Cursada:
    """Model para a entidade Disciplina_Cursada."""

    def __init__(self, 
                 id: int,
                 disciplina: Disciplina,
                 curso_matriculado: Curso_Matriculado,
                 prova1: float,
                 prova2: float,
                 trabalho: float,
                 media: float,
                 faltas: int,
                 frequencia: int,
                 situacao: str) -> None:
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
