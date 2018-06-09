import sys
import time

nomes = ['Alison', 'Mauricio', 'Michel', 'Magno', 'Roselena']

#for nome in nomes:
#    print(nome)

#for i in range(len(nomes)):
#   print(nomes[i])

#for i in range(10000):
#    print(i)

i = 0

#while i < 10:
#    print('i ainda e menor que 10: ', i)
#    i = i + 1

'''EXERCICIO: Faça um programa que leia a quantidade de pessoas que serão convidadas
para uma festa. Após isso o programa irá perguntar o nome de todas as pessoas e colocar 
numa lista de convidados. 
Após isso irá imprimir todos os nomes da lista'''

qtd_convidados = int(raw_input('Quantos convidados para a festa ? '))
lista = []

while qtd_convidados > 0:
    lista.append(str(raw_input('Nome convidado: ')))
    qtd_convidados -= 1

print('Gerando sua lista...')
time.sleep(5)
print('Lista pronta!')

convite = 1

for nome in lista:
    print('Convidado ' + str(convite) + '. - ' + nome)
    convite += 1
