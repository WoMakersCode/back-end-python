# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.__nome = nome
        self.__telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @abstractmethod
    def possui_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def possui_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def possui_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self, clientes):
        self.__clientes = clientes
        self.__saldo = 0
        self.__operacoes = []

    @property
    def saldo(self):
        return self.__saldo

    @property
    def operacoes(self):
        return self.__operacoes

    def deposito(self, valor):
        self.__saldo += valor
        self.__operacoes.append(f'Depósito: +{valor}')

    def saque(self, valor):
        if self.__saldo - valor >= -self.__clientes[0].renda_mensal or self.__clientes[0].possui_cheque_especial():
            self.__saldo -= valor
            self.__operacoes.append(f'Saque: -{valor}')
        else:
            print("Operação não permitida. Saldo insuficiente e sem cheque especial.")

# Exemplo de uso:
cliente_mulher = ClienteMulher("Maria", "123456789", 5000)
conta_mulher = ContaCorrente([cliente_mulher])

cliente_homem = ClienteHomem("João", "987654321", 6000)
conta_homem = ContaCorrente([cliente_homem])

conta_mulher.deposito(1000)
conta_mulher.saque(2000)
print(f"Saldo da conta de {cliente_mulher.nome}: {conta_mulher.saldo}")
print(f"Operações da conta de {cliente_mulher.nome}: {conta_mulher.operacoes}")

conta_homem.deposito(1500)
conta_homem.saque(2000)
print(f"Saldo da conta de {cliente_homem.nome}: {conta_homem.saldo}")
print(f"Operações da conta de {cliente_homem.nome}: {conta_homem.operacoes}")
