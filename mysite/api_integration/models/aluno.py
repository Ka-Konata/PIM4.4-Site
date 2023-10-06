from typing import Any
from .pessoa import Pessoa

class Aluno(Pessoa):
    """Model para a entidade Aluno, herda Pessoa."""

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
    