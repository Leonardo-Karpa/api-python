class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        
    @property
    def marca(self): return self.__marca
    
    @property
    def modelo(self): return self.__modelo
    
    @property
    def ano(self): return self.__ano
    
    def descrever(self):
        return f'{self.__marca} {self.__modelo} ({self.__ano})'
    
    def __str__(self):
        return self.descrever()
    
class Carro(Veiculo): # ele herda o véiculo
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano) # Chama o __init__ do Pai
        self.__num_portas = num_portas
        
    @property
    def num_portas(self): 
        return self.__num_portas
    
    def descrever(self): # Sobrescreve o pai
        base = super().descrever()
        return f'{base} | {self.__num_portas} portas'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas): # herda veiculo
            super().__init__(marca, modelo, ano)
            self.__cilindradas = cilindradas
            
    @property
    def cilindradas(self): return self.__cilindradas
    
    def descrever(self): # Sobrescreve o pai
        base = super().descrever()
        return f'{base} | {self.__cilindradas}cc'
    
# Testes

C = Carro('Jeep', 'Compass', 2023, 4)
m = Moto('Kawasaki', 'CG 220', 2022, 220)

print(C) # Jeep Compass (2023) | 4 Portas
print(m) # Kawasaki CG 220 | 220cc
print(C.marca) # Jeep - herdado do Pai
print(isinstance(C, Veiculo)) # True - Carro é um veiculo
print(isinstance(m, Carro)) # False - Moto não é um Carro
