from typing import TypeVar, Generic, Tuple

T = TypeVar('T')
U = TypeVar('U')

class Par(Generic[T, U]):
    def __init__(self, primero: T, segundo: U) -> None:
        self.primero = primero
        self.segundo = segundo
    
    def intercambiar(self) -> 'Par[U, T]':
        return Par(self.segundo, self.primero)
    
    def __str__(self) -> str:
        return f"Par({self.primero}, {self.segundo})"

# Uso
par1 = Par("Kirey", 25)
par2 = Par(6.2, [1, 2, 3])

print(par1)  
print(par2)  
