from typing import Any
from .pessoa import Pessoa

class Professor(Pessoa):
    """Model para a entidade Professor, herda Pessoa."""

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
    