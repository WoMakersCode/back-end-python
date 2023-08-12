# Erros de sintaxe sempre interrompem a execução do programa.
quantidade = 10000
print('quantidade:', quantidade)

# if(quantidade = 3000)
# print("Você tem 3000 dinheiros.")

# Exceções são lançadas por erros de lógica
# quantidade = quantidade / 0

# Tratamento de exceções
print('Tratamento de exceções - except genérico')
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

def executar_pato(animal):
    try:
        animal.quack()
        animal.andar()
        animal.voar()
        animal.nadar()
    except AttributeError as e:
        print(f'Erro de atributo: {e}')

pato = Pato()
calopsita = Calopsita()

executar_pato(pato)
executar_pato(calopsita)

print('Continuando a execução...')