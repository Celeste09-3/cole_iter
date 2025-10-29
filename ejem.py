from typing import TypeVar, Generic, List, Iterator
from dataclasses import dataclass

# definir clases genéricas
T = TypeVar('T')

# MODELO DE DATOS

@dataclass
class Libro:
    """Representa un libro con título, autor, ISBN y año de publicación"""
    titulo: str
    autor: str
    isbn: str
    año_publicacion: int

    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} ({self.año_publicacion})"

# COLECCIÓN GENÉRICA

class Coleccion(Generic[T]):
    """Colección genérica que almacena elementos de tipo T"""

    def __init__(self) -> None:
        self._elementos: List[T] = []

    def agregar(self, elemento: T) -> None:
        """Agrega un elemento a la colección"""
        self._elementos.append(elemento)

    def __len__(self) -> int:
        return len(self._elementos)

    def __getitem__(self, index: int) -> T:
        """Permite acceder a elementos por índice (como una lista)"""
        return self._elementos[index]

    def __iter__(self) -> Iterator[T]:
        """Permite iterar sobre la colección con un bucle for"""
        return iter(self._elementos)

# ITERADOR FILTRADO

class IteradorFiltrado(Generic[T]):
    """Iterador que recorre una colección y devuelve solo los elementos que cumplen una condición"""

    def __init__(self, coleccion: Coleccion[T], condicion) -> None:
        self._coleccion = coleccion
        self._condicion = condicion
        self._index = 0

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        while self._index < len(self._coleccion):
            elemento = self._coleccion[self._index]
            self._index += 1
            if self._condicion(elemento):
                return elemento
        raise StopIteration  # Fin de la iteracion

# SISTEMA

class SistemaBiblioteca:
    """Sistema que gestiona una colección de libros y permite búsquedas"""

    def __init__(self) -> None:
        self.libros: Coleccion[Libro] = Coleccion()

    def agregar_libro(self, libro: Libro) -> None:
        """Agrega un libro a la colección principal"""
        self.libros.agregar(libro)

    def buscar_libros_por_titulo(self, texto: str) -> Iterator[Libro]:
        """Devuelve un iterador con libros cuyo título contiene el texto dado"""
        return IteradorFiltrado(self.libros, lambda l: texto.lower() in l.titulo.lower())

# USO

def main():
    biblioteca = SistemaBiblioteca()

    # libros de ejemplo
    biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", "978-8437604947", 1967))
    biblioteca.agregar_libro(Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "978-0307474728", 1985))
    biblioteca.agregar_libro(Libro("1984", "George Orwell", "978-0451524935", 1949))

    print("Todos los libros:")
    for libro in biblioteca.libros:
        print(f" - {libro}")

    print("\n Libros que contienen 'amor' en el título:")
    for libro in biblioteca.buscar_libros_por_titulo("amor"):
        print(f" - {libro}")

if __name__ == "__main__":
    main()
