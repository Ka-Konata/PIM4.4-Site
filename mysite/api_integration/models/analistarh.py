from typing import Any
from .pessoa import Pessoa

class AnalistaRH(Pessoa):
    """Model para a entidade AnalistaRH, herda Pessoa."""
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
    