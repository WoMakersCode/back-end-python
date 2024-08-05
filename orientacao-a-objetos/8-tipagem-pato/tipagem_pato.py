# Uma mesma variável em python pode ter valores de tipos diferentes
a = 1
a = "Maria"

class Ave():
    def andar(self):
        print('andando')

    def voar(self):
        print('voando')

class Calopsita(Ave):
    def piar(self):
        print('piuuuu')

class Pato(Ave):
    def quack(self):
        print('quack')

    def nadar(self):
        print('nadando')

# Como as variáveis não são tipadas, não é possível saber o tipo de uma variável em uma função
# A função não tem como garantir que o animal é de algum tipo específico, por exemplo, o tipo `Pato`
def executar_pato(animal):
    animal.quack()
    animal.andar()
    animal.voar()
    animal.nadar()

pato = Pato()
calopsita = Calopsita()

executar_pato(pato)
#executar_pato(calopsita)
