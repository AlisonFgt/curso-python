from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 60:
            print('Erro: Tanque com incapacidade inferior!') #SOBREPOSICAO
        else:
            self.tanque += litros

