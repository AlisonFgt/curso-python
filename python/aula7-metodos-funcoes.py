'''EXERCICIO: Escreva uma função que recebe um objeto de coleção e retorna o valor
do maior numero dentro dessa colecao faça outra função que retorna o menor número
dessa coleação'''

numeros = [0, 5, 6, 8, 10, -2, 55]

def maior_numero(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior: 
            maior = numero
    return maior

def menor_numero(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor: 
            menor = numero
    return menor

print('Maior número da lista ' + str(maior_numero(numeros)))
print('Menor número da lista ' + str(menor_numero(numeros)))