# Um risco de importar tudo é ter uma outra função ou variável no namespace
# atual com o mesmo nome. Neste caso, é fácil ter um bug porque você pode
# ao invés de usar um método, o programador acaba usando o outro.
from funcoes_do_log import *

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!') # usa a função que foi importada
print()

def imprimir_no_log(texto): # sobrescreve a função importada do módulo "funcoes_do_log"
    print(texto)

imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')
