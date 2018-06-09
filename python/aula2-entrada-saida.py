'''nome = "Alison"
tipo = type(nome)
idade = 28
tipo_idade = type(idade)
altura = 1.75
tipo_altura = type(altura)

print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura)  + ' de altura')

nome = raw_input('Escreva seu nome: ')
idade = raw_input('Escreva sua idade: ')
altura = raw_input('Escreva sua altura : ')

print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura)  + ' de altura')

numero1 = 10
numero2 = 30
numero3 = 74.8

resultado = numero1 + numero2 / numero3

print(resultado)

EXEXCICIO: Faça um formulario que pergunte o nome, cpf, endereco, idade, altura e telefone
e imprima isso em um relatório organizado. '''

nome = raw_input('Escreva seu nome: ')
cpf = raw_input('Escreva seu cpf: ')
endereco = raw_input('Escreva seu endereço: ')
idade = raw_input('Escreva sua idade: ')
altura = raw_input('Escreva sua altura : ')
telefone = raw_input('Escreva seu telefone: ')

print('Nome: ' + nome + '\nCPF: ' + cpf + '\nEndereço: ' + endereco + '\nIdade: ' + idade + '\nAltura: ' + altura + '\nTelefone: ' + telefone)