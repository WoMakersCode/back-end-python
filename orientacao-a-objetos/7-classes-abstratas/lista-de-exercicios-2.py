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

from abc import ABC, abstractmethod #abc fornece classe e métodos abstratos, ABC marca métodos que devem ser implementados pelas subclasses

# Classe abstrata Cliente estrutura para todos s clientes
class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):# construtor __init__ inicializa os atributos
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property #propriedade nome
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property #propriedade telefone
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value

    @property #propriedade renda mensal
    def renda_mensal(self):
        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, value):
        self._renda_mensal = value

    @abstractmethod
    def cliente_info(self):
        pass

class ClienteMulher(Cliente):#herda da classe absrata cliente
    def __init__(self, nome, telefone, renda_mensal):#inicializa os atributos e cria o objeto cheque especia
        super().__init__(nome, telefone, renda_mensal)
        self._cheque_especial = ChequeEspecial(self._renda_mensal)
        
    @property #permite accesso ao objeto cheque especial
    def cheque_especial(self):
        return self._cheque_especial

    def cliente_info(self):#meto abstrato da classe e retorna uma string
        return f'Cliente Mulher: {self._nome}, Telefone: {self._telefone}, Renda Mensal: {self._renda_mensal}'

class ClienteHomem(Cliente):#herda a classe cliente
    def cliente_info(self):# implementa o metodo cliente info
        return f'Cliente Homem: {self._nome}, Telefone: {self._telefone}, Renda Mensal: {self._renda_mensal}'

class ChequeEspecial: # inicializa o limite cheque especiall
    def __init__(self, limite):
        self._limite = limite

    @property # acesso e modificação cheque especial
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = value

    def verificar_cheque_especial(self):#retorna stringo com o limite disponível do cheque especial
        return f'Cheque especial disponível até {self._limite}'

class ContaCorrente: # inicializa a lista de clientes, saldo da conta e operações
    def __init__(self, clientes, saldo):
        self._clientes = clientes
        self._saldo = saldo
        self._operacoes = []

    @property # acesso e modificação saldo
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    def deposito(self, valor):# adiciona valor ao saldo
        if valor > 0:
            self._saldo += valor
            self._operacoes.append(f'Depósito de {valor}')
            print(f'Depósito de {valor} realizado com sucesso. Saldo atual: {self._saldo}.')
        else:
            print('O valor do depósito deve ser positivo.')

    def saque(self, valor):# realiza saque se valor for suficiente
        if valor > 0:
            cheque_especial_limite = 0
            # Verifica se algum cliente é do tipo ClienteMulher e define o limite do cheque especial
            for cliente in self._clientes:
                if isinstance(cliente, ClienteMulher):
                    cheque_especial_limite = cliente.cheque_especial.limite
                    break
            
            if self._saldo - valor >= -cheque_especial_limite:
                self._saldo -= valor
                self._operacoes.append(f'Saque de {valor}')
                print(f'Saque de {valor} realizado com sucesso. Saldo atual: {self._saldo}.')
            else:
                print('Saldo insuficiente para o saque.')
        else:
            print('O valor do saque deve ser positivo.')

    def exibir_info_clientes(self): #exibe informações dos clientes
        for cliente in self._clientes:
            print(cliente.cliente_info())

    def exibir_operacoes(self): # exie operações realizadas
        for operacao in self._operacoes:
            print(operacao)

# Criar clientes (instância)
cliente1 = ClienteMulher('Maria', '11988888888', 3000.00)
cliente2 = ClienteHomem('João', '11999999999', 2000.00)

# Criar uma conta corrente com os clientes (instância)
conta_corrente = ContaCorrente([cliente1, cliente2], 5000.00)

# Usar os métodos da conta corrente
conta_corrente.exibir_info_clientes()
conta_corrente.deposito(1000.00)  # Depósito de 1000
conta_corrente.saque(1500.00)     # Saque de 1500
conta_corrente.exibir_operacoes() # Verificar operações realizadas
