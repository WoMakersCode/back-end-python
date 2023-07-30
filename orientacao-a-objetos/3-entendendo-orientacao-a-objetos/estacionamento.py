class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

class Moto:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

class Vaga:
    def __init__(self, identificador, tipo):
        self.id = identificador
        self.livre = True

        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')

        self.tipo = tipo
        self.placa = None

    def ocupar(self, placa):
        if self.livre is False:
            raise ValueError(f'A vaga {self.identificador} já está ocupada')

        self.placa = placa
        self.livre = False

    def desocupar(self):
        if self.livre is True:
            raise ValueError(f'A vaga {self.identificador} já está livre')

        self.placa = None
        self.livre = True


class Estacionamento:
    def __init__(self, total_vagas_livres_carro, total_vagas_livres_moto):
        self.carro_para_vaga = {}
        self.moto_para_vaga = {}
        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livres_moto
        self.inicializar_vagas()

    def inicializar_vagas(self):
        self.vagas_carro = {} # id da vaga para a placa do carro
        self.vagas_moto = {} # id da vaga para a placa da moto

        tipo = 'carro'
        for i in range(self.total_vagas_livres_carro):
            self.vagas_carro[i] = Vaga(i, tipo)
        
        primeiro_id_motos = self.total_vagas_livres_carro
        ultimo_id_motos = primeiro_id_motos + self.total_vagas_livres_moto
        tipo = 'moto'
        for j in range(primeiro_id_motos, ultimo_id_motos):
            self.vagas_moto[j] = Vaga(j, tipo)

    def estacionar_carro(self, carro: Carro):
        if carro.estacionado is True:
            raise ValueError(f'O carro {carro.placa} já está no estacionamento.')

        id_da_proxima_vaga, tipo = self.buscar_id_da_proxima_vaga_livre('carro') # gera o id da próxima vaga
        if id_da_proxima_vaga is None:
            raise ValueError(f'Não há mais vagas de carro disponíveis no estacionamento.')
        elif id_da_proxima_vaga is not None and tipo is 'carro':
            vaga = self.vagas_carro[id_da_proxima_vaga]
            vaga.ocupar(carro.placa)
            carro.estacionar()
            self.carro_para_vaga[carro.placa] = vaga.id # permite achar imediatamente em qual vaga está a carro
            self.total_vagas_livres_carro -= 1 # reduz o número de vagas livres
        else:
            raise RuntimeError(f'Erro interno - não foi possível recuperar a próxima vaga de carro.')
        
        print(f'Carro {carro.placa} estacionado na vaga {vaga.id} do tipo {vaga.tipo}')


    def estacionar_moto(self, moto: Moto):
        if moto.estacionado is True:
            raise ValueError(f'O carro {moto.placa} já está no estacionamento.')

        id_da_proxima_vaga, tipo = self.buscar_id_da_proxima_vaga_livre('moto') # gera o id da próxima vaga

        if id_da_proxima_vaga is None:
            raise ValueError(f'Não há mais vagas de moto disponíveis no estacionamento.')
        elif id_da_proxima_vaga is not None and tipo is 'moto':
            vaga = self.vagas_moto[id_da_proxima_vaga]
            vaga.ocupar(moto.placa)
            moto.estacionar()
            self.moto_para_vaga[moto.placa] = vaga.id # permite achar imediatamente em qual vaga está a moto
            self.total_vagas_livres_moto -= 1 # reduz o número de vagas livres
        elif id_da_proxima_vaga is not None and tipo is 'carro':
            vaga = self.vagas_carro[id_da_proxima_vaga]
            vaga.ocupar(moto.placa)
            moto.estacionar()
            self.moto_para_vaga[moto.placa] = vaga.id # permite achar imediatamente em qual vaga está a moto
            self.total_vagas_livres_carro -= 1 # reduz o número de vagas livres
        else:
            raise RuntimeError(f'Erro interno - não foi possível recuperar a próxima vaga de moto.')

        print(f'Moto {moto.placa} estacionada na vaga {vaga.id} do tipo {vaga.tipo}')

    def buscar_id_da_proxima_vaga_livre(self, tipo):
        if tipo == 'carro':
            if self.total_vagas_livres_carro > 0:
                for identificador in self.vagas_carro.keys():
                    vaga = self.vagas_carro[identificador]
                    if vaga.livre is True:
                        return identificador, 'carro'
            else:
                # Não achou vaga de carro
                return None, ''
        elif tipo == 'moto':
            if self.total_vagas_livres_moto > 0:
                for identificador in self.vagas_moto.keys():
                    vaga = self.vagas_moto[identificador]
                    if vaga.livre is True:
                        return identificador, 'moto'
            if self.total_vagas_livres_carro > 0:
                for identificador in self.vagas_carro.keys():
                    vaga = self.vagas_carro[identificador]
                    if vaga.livre is True:
                        return identificador, 'carro'
            # Não achou vaga de carro nem de moto
            return None, ''
        else:
            raise TypeError(f'Tipo {tipo} não reconhecido')

    def remover_carro(self, carro: Carro):
        id_vaga = self.carro_para_vaga[carro.placa]
        vaga = self.vagas_carro[id_vaga]
        vaga.desocupar()
        carro.sair_da_vaga()
        del self.carro_para_vaga[carro.placa]
        self.total_vagas_livres_carro += 1
        print(f'Carro {carro.placa} retirado da vaga {vaga.id}')
        return True

    def remover_moto(self, moto: Moto):
        id_vaga = self.moto_para_vaga[moto.placa]
        vaga = None

        if id_vaga in self.vagas_moto:
            vaga = self.vagas_moto[id_vaga]
        elif id_vaga in self.vagas_carro:
            vaga = self.vagas_carro[id_vaga]
        else:
            raise ValueError(f'Não foi possível encontrar a vaga com identificador {id_vaga}')

        moto.sair_da_vaga()
        vaga.desocupar()
        del self.moto_para_vaga[moto.placa]

        if vaga.tipo == 'moto':
            self.total_vagas_livres_moto += 1
        else:
            self.total_vagas_livres_carro += 1

        print(f'Moto {moto.placa} retirada da vaga {vaga.id} (tipo {vaga.tipo})')

    def estado_do_estacionamento(self):
        num_carros_estacionados = len(self.carro_para_vaga)
        num_motos_estacionadas = len(self.moto_para_vaga)
        estado = ' ---- Estado do estacionamento ----\n'
        estado += f'  Num carros estacionados: {num_carros_estacionados}\n'
        estado += f'  Num motos estacionadas: {num_motos_estacionadas}\n'
        estado += f'  Total de vagas livres de carros: {self.total_vagas_livres_carro}\n'
        estado += f'  Total de vagas livres de motos: {self.total_vagas_livres_moto}\n'
        estado += f'  Vagas de carro:\n    '
        for i in range(len(self.vagas_carro)):
            placa = self.vagas_carro[i].placa
            estado += f'vaga[{i}]: {placa}; '
        estado += f'\n  Vagas de moto:\n    '
        id_primeira_vaga_moto = len(self.vagas_carro)
        id_ultima_vaga_moto = id_primeira_vaga_moto + len(self.vagas_moto)
        for i in range(id_primeira_vaga_moto, id_ultima_vaga_moto):
            placa = self.vagas_moto[i].placa
            estado += f'vaga[{i}]: {placa}; '
        estado += '\n ----------------------------------\n'
        return estado

    def __str__(self):
        return self.estado_do_estacionamento()