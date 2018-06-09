from cliente import Cliente

class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def sacar(valor):
        if(self.saldo >= valor):
            self.saldo -= valor
            print('Sacado ' + str(valor) + ' reais.')
        else:
            print('Saldo insuficiente!')

    def depositar(self, valor):
        if(valor > 0):
            self.saldo += valor
            print('Foi depositado: ' + str(valor))
        else:
            print('Erro no deposito')

    def consulta_saldo(self):
        return str(self.saldo)

    def sacar(self, valor):
        if(self.saldo - valor < self.limite):
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print('Foi sacado: ' + str(valor))