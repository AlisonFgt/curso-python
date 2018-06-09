'''EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura da de uma pessoa 
e decide se ela está apta a ser do Exercito para entrar no Exercito é preciso 
ter mais de 18 anos pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70 metros'''

idade = raw_input('Qual a sua idade: ')
peso = raw_input('Qual o seu peso: ')
altura = raw_input('Qual a sua altura: ')

apto = True

if int(idade) < 18:
    apto = False
elif float(altura) < 1.70:
    apto = False
elif int(peso) < 60:
    apto = False

messagem = 'Apto ao serviço militar!'

if apto == False:
    messagem = 'Você não está apto ao serviço militar!'

print(messagem)


