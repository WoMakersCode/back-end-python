# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            print("O carro está ligado.")
            self.ligado = True
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            print("O carro está desligado.")
            self.ligado = False
            self.velocidade = 0
        else:
            print("O carro já está desligado.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")
        else:
            print("O carro está desligado. Não é possível acelerar.")

    def desacelerar(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
            print(f"O carro desacelerou. Velocidade atual: {self.velocidade} km/h")
        elif self.velocidade == 0:
            print("O carro já está parado.")
        else:
            print("O carro está desligado. Não é possível desacelerar.")


# Crie uma instância da classe Carro.
meu_carro = Carro(cor="Vermelho", modelo=2023)

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.acelerar()

# Faça o carro "parar" utilizando os métodos da sua classe.
meu_carro.desacelerar()
meu_carro.desligar()
