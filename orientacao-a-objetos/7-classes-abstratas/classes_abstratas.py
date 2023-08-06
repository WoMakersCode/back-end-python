from abc import ABC, abstractmethod

# A classe base dos pokemons
class BasePokemon(ABC):
    def __init__(self, nome):
        self.nome = nome
        self._nivel = 1
        self._experiencia = 0

    @abstractmethod
    def ataque_principal(self): # O uso de métodos abstratos torna a classe abstrata
        pass

    @abstractmethod
    def passar_de_nivel(self):
        pass

    @abstractmethod
    def evoluir(self):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass

# Criar um objeto de uma classe abstrata gera um erro
# pokemon = BasePokemon('Pikachu', 'Elétrico')

class Pikachu(BasePokemon):
    def ataque_principal(self):
        print(f'{self.nome} usou Choque de trovão!')
        self._experiencia += 2
        self.passar_de_nivel()

    def passar_de_nivel(self):
        # Passa de nível a cada 10 pontos de experiência
        if self._experiencia % 10 == 0:
            self._nivel += 1
            print(f'{self.nome} passou para o nível {self._nivel}!')
            self.evoluir()

    def evoluir(self):
        if self._nivel == 25:
            print('!!!! Evoluiu para Raichu !!!!')
            self.nome = 'Raichu'

    @property
    def tipo(self):
        return 'Elétrico'
    
    def ataque_secundario(self):
        print(f'{self.nome} usou Surra de Calda!')
        self._experiencia += 2
        self.passar_de_nivel()

pokemon = Pikachu('Pikachu')
print(pokemon.nome + ' é um pokemon do tipo ' + pokemon.tipo)
for _ in range(125):
    pokemon.ataque_principal()
    pokemon.ataque_secundario()