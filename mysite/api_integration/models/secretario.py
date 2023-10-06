from typing import Any
from .pessoa import Pessoa

class Secretario(Pessoa):
    """Model para a entidade Secretario, herda Pessoa."""

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
    