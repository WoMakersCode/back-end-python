# Pessoa é a nossa classe base
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print('Oi! Meu nome é {}'.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Naira')
pessoa.falar_oi()
pessoa.falar_tipo()
print()

# A classe estudante é derivada da classe Pessoa.
# Relação é: "Estudante" é uma "Pessoa"
class Estudante(Pessoa): # o nome da classe base vem em parênteses
    def __init__(self, name, curso):
        super().__init__(name) # chama o construtor da classe base
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso "{self._curso}"') # A propriedade self._nome é herdada da classe base
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        self._tipo = 'Estudante'
        return super().falar_tipo()

estudante = Estudante('Yasmin', 'Introdução ao Python')
estudante.falar_oi() # o método "falar_oi" é herdado da classe base
estudante.falar_tipo() # o método "falar_tipo" é herdado da classe base, e sobrescrito na classe derivada
estudante.falar_curso()
print()

# Podemos testar se um objeto é de um determinado tipo em tempo de execução com as funções abaixo
print('O objeto estudante é uma instância da classe Estudante? ', isinstance(estudante, Estudante))
print('O objeto estudante é uma instância da classe Pessoa? ', isinstance(estudante, Pessoa))
print('A classe Estudante é uma sub-classe de Pessoa? ', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe de Estudante? ', issubclass(Pessoa, Estudante))
print()

# Herança transitiva
class Trabalhador(Pessoa): # Trabalhador também herda de Pessoa
    def __init__(self, nome, profissao):
        super().__init__(nome) # chama o construtor da classe base
        self.__profissao = profissao # atributo privado - só pode ser acessado dentro da classe Trabalhador
        self._tipo = 'Trabalhador'

    def falar_profissao(self):
        print(f'Eu, {self._nome}, exerço a profissão "{self.__profissao}"')
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        return super().falar_tipo()

class Professor(Trabalhador): # Professor herda de Trabalhador
    def __init__(self, nome, disciplina):
        super().__init__(nome, 'Professor') # chama o construtor da classe base
        self.__disciplina = disciplina

    def falar_profissao(self):
        self.__profissao = 'Instrutora' # variáveis privadas não conseguem ser alteradas pela classe derivada
        return super().falar_profissao()

    def falar_disciplina(self):
        print(f'Eu, {self._nome}, dou aulas da disciplina "{self.__disciplina}"')
    
    def falar_tipo(self): # Sobrescreve a função original da classe Pessoa
        self._tipo = 'Professor'
        return super().falar_tipo()

trabalhadora = Trabalhador('Beatriz', 'Desenvolvedora')
trabalhadora.falar_oi()
trabalhadora.falar_tipo()
trabalhadora.falar_profissao()
print()

professora = Professor('Clarisse', 'Python')
professora.falar_oi()
professora.falar_tipo()
professora.falar_profissao()
professora.falar_disciplina()
print()

# Em Python, todos as classes herdam implicitamente da classe object
class Humano:
    pass

# A classe Humano já começa com vários atributos e métodos
humano = Humano()
print(dir(humano))
print()

# Esses mesmos atributos e métodos existem nas classes que declaramos acima
print(dir(professora))
print()