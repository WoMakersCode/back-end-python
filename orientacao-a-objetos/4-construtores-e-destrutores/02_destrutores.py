# Construtor padrão
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome
        print(f'MinhaClasse1: Chamou o construtor padrão de {nome}')

    def __del__(self):
        print(f'MinhaClasse1: Chamou o destrutor de {self.nome}')

# O momento de execução de um destrutor é depois que o programa tem seu encerramento solicitado
print('Começou a execução do programa')
objeto1 = MinhaClasse('objeto1')
print('Vai terminar a execução do programa')
exit()

# Quando todas as referências a um objeto são excluídas, ele o destrutor é automaticamente chamado
print('Começou a execução do programa')
objeto1 = MinhaClasse('objeto1')
objeto2 = MinhaClasse('objeto2')
del objeto1
print('Vai terminar a execução do programa')