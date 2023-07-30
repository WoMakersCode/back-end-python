from estacionamento import *
from random import randint

# Inicializa duas lista com motos e carros
carros = []
for i in range(10):
    placa = randint(1000, 9999)
    carros.append(Carro(placa))
motos = []
for i in range(20):
    placa = randint(1000, 9999)
    motos.append(Moto(placa))

# Inicializa o estacionamento e imprime seu estado
estacionamento = Estacionamento(5, 5)
print(estacionamento)

# Estaciona 4 carros
for i in range(4):
    estacionamento.estacionar_carro(carros[i])
print(estacionamento)

# Estaciona 6 motos
for i in range(6):
    estacionamento.estacionar_moto(motos[i])
print(estacionamento)

# Tenta estacionar mais um carro mas o estacionamento está cheio
# estacionamento.estacionar_carro(carros[4])

# Um carro sai do estacionamento e libera uma vaga para carros
estacionamento.remover_carro(carros[0])
print(estacionamento)

# Tenta estacionar uma moto que já está no estacionamento
# estacionamento.estacionar_moto(motos[5])

# Estaciona uma nova moto
estacionamento.estacionar_moto(motos[6])
print(estacionamento)

# Um carro e uma moto deixam o estacionamento
estacionamento.remover_carro(carros[1])
estacionamento.remover_moto(motos[3])
print(estacionamento)

# Chega uma nova moto - deve usar preferencialmente a vaga de moto que foi liberada anteriormente
estacionamento.estacionar_moto(motos[7])
print(estacionamento)