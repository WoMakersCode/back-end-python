# Definição da classe
class Televisao: # Conveção para nomes de classes: PascalCasing
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False
    
    def mudar_canal_para_cima(self):
        if not self.ligada:
            return

        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return

        if self.canal > self.canal_max:
            self.canal -= 1
        
    def aumentar_volume(self):
        if not self.ligada:
            return

        if self.volume < self.volume_max:
            self.volume += 10

    def reduzir_volume(self):
        if not self.ligada:
            return

        if self.volume > self.volume_min:
            self.volume -= 10

    def __str__(self) -> str:
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'

# Criando instâncias da class Televisao
tv_sala = Televisao()
tv_quarto = Televisao()

# Quando chamamos o método ligar() em uma instância, estamos alterando o estado apenas
# dela. A outra televisão permanece desligada.
tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada))

for _ in range(3):
    tv_sala.aumentar_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))
print()

# Se tentamos imprimir o conteúdo do objeto, visualizamos uma representação estranha.
print('tv_sala:', tv_sala)
print('tv_quarto:', tv_quarto)
print()

# O método especial `__str__()` permite que nós criemos uma representação em string para
# uma instância que tenha o tipo definido pela nossa classe.
print('tv_sala:', tv_sala)
print('tv_quarto:', tv_quarto)
print()

# Já usamos classes antes quando falamos de tipos de dados relativos a datas
from datetime import date

# Dia é um objeto, ou seja, uma instância da classe date
dia = date(2019, 2, 22)
print('Dia da semana:', dia.weekday())