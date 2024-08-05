# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:  # Classe
    def __init__(self, cor, modelo, velocidade=100):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        
    def ligar(self):
        self.ligado = True
        
    def desligar(self):
        self.ligado = False
            
    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            
    def desacelerar(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10

# Criando uma instância da classe Carro
carro = Carro(cor="vermelho", modelo="Brasilia")

# Usando os métodos
carro.ligar()
print(f'Carro ligado: {carro.ligado}')

carro.acelerar()
print(f'Velocidade após acelerar: {carro.velocidade}')

carro.desacelerar()
print(f'Velocidade após desacelerar: {carro.velocidade}')

carro.desligar()
print(f'Carro desligado: {carro.ligado}')

# Acessando e imprimindo atributos
print(f'Cor do carro: {carro.cor}')
print(f'Modelo do carro: {carro.modelo}')
