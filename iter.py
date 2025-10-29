class Contador:
    def __init__(self, limite: int):
        self.limite = limite
        self.inicio = 5
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.inicio < self.limite:
            resultado = self.inicio
            self.inicio += 1
            return resultado
        raise StopIteration

# Uso
contador = Contador(17)
for numero in contador:
    print(numero)  