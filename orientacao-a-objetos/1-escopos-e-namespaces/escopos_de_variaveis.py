# Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e
# com variáveis externas ou globais. A diferença entre elas é a visibilidade ou escopo.

# 'comida' é uma variável é LOCAL porque só existe dentro do escopo da função "cardapio".
def cardapio():
    comida = 'hamburguer'
    print(comida)

# print(comida) # essa linha vai gerar um erro

# Variáveis declaradas fora de qualquer função são chamadas de GLOBAIS. Elas
# se encontram em um escopo que é acessível por qualquer função neste script.
bebida = 'refrigerante'
def cardapio():
    comida = 'hamburguer'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print()

# Ao alterar o valor de uma variável global dentro de uma função, na verdade é criada
# outra variável com o mesmo nome dentro do escopo da função e a variável global
# permanece intacta.
bebida = 'refrigerante'
def cardapio():
    comida = 'hamburguer'
    bebida = 'suco'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida)
print()

# Para alterar o valor de uma variável global dentro de uma função, precisamos informar
# a função que vamos utilizar a variável do escopo global.
bebida = 'refrigerante'
def cardapio():
    global bebida
    comida = 'hamburguer'
    bebida = 'suco'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida)
print()
