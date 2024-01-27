from funcoes_do_log_colorido import imprimir_no_log

imprimir_no_log('teste', 'info')
imprimir_no_log('teste', 'aviso')
imprimir_no_log('teste', 'erro')
imprimir_no_log('teste', 'outro')

import funcoes_do_log_colorido
funcoes_do_log_colorido.imprimir_no_log(f'Bem vinda, {funcoes_do_log_colorido.nome_de_usuario}!', 'erro')
