# Este arquivo consiste no módulo "funcoes_do_log"

nome_de_usuario = 'Dori'

def imprimir_no_log(texto, nivel='info'):
    if nivel.lower() == 'info':
        print(f'Info: {texto}')
    elif nivel.lower() == 'aviso':
        print(f'Aviso: {texto}')
    elif nivel.lower() == 'erro':
        print(f'Erro: {texto}')
    else:
        print('Erro interno - nível desconhecido de mensagem')