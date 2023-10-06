from typing import Any


class A:
    def __init__(self, x, y) -> None:
        print(f"x: {x}, y: {y}")

    def by_dict(d) -> None:
        r = A(
            x=d["x"] if "x" in d.keys() else None, 
            y=d["y"] if "y" in d.keys() else None)
        return r

class B(A):
    #def __call__(self, *args: Any, **kwds: Any) -> Any:
        #return super().__call__(*args, **kwds)
    
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

d = {"a": 1, "y": 2}
a = A.by_dict(d)
b = B.by_dict(d)