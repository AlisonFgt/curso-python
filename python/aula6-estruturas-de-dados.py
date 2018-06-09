minha_lista = ['Gui', 'Joao']                       # LISTA (list)
minha_tupla = ('Gui', 'Joao')                       # TUPLA (tuple) 
meu_dicionario = {'nome': 'Guilherme', 'idade': 27} # DICIONARIO (dict)
meu_conjunto = {'Gui', 'Joao'}                      # CONJUNTO (set)

conjunto_vazio = set()
tuplas = [(1,2), (3,4), (5,6), ({'Joao', 'Maria'}, {'Grabiel'})]

print(tuplas)

#print(meu_dicionario['nome'])
#print(meu_dicionario['idade'])

meu_dicionario['endereco'] = 'Rua Novo Hamburgo'

#print(meu_dicionario.values())

meu_conjunto.add('Gui') # Conjunto não adiciona dados repetidos o 'Gui' já existe

#print(meu_conjunto)

#if 'Gui' in meu_conjunto:   # Perfomatico para pesquisa (conjunto e dicionario)
#    print('Foi encontrado!')

meu_conjunto.remove('Gui')