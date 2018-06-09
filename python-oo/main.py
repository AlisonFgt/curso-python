from veiculo import Veiculo
from carro import Carro
from cliente import Cliente
from conta import Conta

voyage = Veiculo('prata', 4, 'wolkwagem', 60)

#print('Cor: ' + voyage.cor + '\nMarca: ' +  voyage.marca + '\nTanque: ' + str(voyage.tanque))

voyage.abastecer(30)

#print('Cor: ' + voyage.cor + '\nMarca: ' +  voyage.marca + '\nTanque: ' + str(voyage.tanque))

#CARRO herda de Veiculo e não precisa passar rodas!! é fixo 4

voyage = Carro('prata', 'wolkwagem', 60)

#print('Cor: ' + voyage.cor + '\nMarca: ' +  voyage.marca + '\nTanque: ' + str(voyage.tanque))

#voyage.abastecer(30)

#print('Cor: ' + voyage.cor + '\nMarca: ' +  voyage.marca + '\nTanque: ' + str(voyage.tanque))

'''EXERCICIO: Crie um software de gerenciamento bancário esse software poderá ser capaz de 
criar clientes e contas, cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo! '''

#Criar cliente

pessoa = Cliente('Alison', '02161828888', '28')

print(pessoa)

#Criar Conta

conta_alison = Conta(pessoa, 700.80, 400)

print(conta_alison.cliente.nome + ' ' + conta_alison.consulta_saldo())

conta_alison.depositar(50.75)

print(conta_alison.consulta_saldo())

conta_alison.sacar(500)

print(conta_alison.consulta_saldo())

conta_alison.sacar(400)

print(conta_alison.consulta_saldo())
