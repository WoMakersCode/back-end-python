# Posso importar também partes específicas do módulo ao invés de importar tudo que
# existe dentro dele. Dessa forma, meu namespace corrente fica mais limpo e meu
# "autocompletar" do VS code fica menos cheio de coisas.
from funcoes_do_log import nome_de_usuario, imprimir_no_log
imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')

# O primeiro datetime é o nome do módulo, o segundo é o nome de uma classe que existe dentro
# desse módulo
from datetime import datetime
agora = datetime.now()