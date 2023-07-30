# Para importar todo o conteúdo do módulo "funcoes_do_log" sem precisar
# utilizar o namespace para usá-lo, podemos utilizar a palavra chave "from".
# O conteúdo do módulo vai ser todo importado para o namespace corrente.
# O asterisco indica que queremos importar todo o conteúdo deste módulo.
from funcoes_do_log import *
imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')