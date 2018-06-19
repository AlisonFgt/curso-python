import requests
import json

req = None

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=7c974ec7&t=' + titulo + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Titulo: ' +  filme['Title'])
    print('Ano: ' + filme['Year'])
    print('Diretor: ' + filme['Director'])
    print('Atores: ' + filme['Actors'])
    print('Nota: ' + filme['imdbRating'])
    print('Premios: ' + filme['Awards'])
    print('Poster: ' + filme['Poster'])
    print('')

sair = False

'''
while not sair:
    op = raw_input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op.upper() == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)


EXERCICIO ABAIXO: Por Alison Alves   '''

def existeFilmes(titulo):
    lista = []
    quant = 0 

    try:
        req = requests.get('http://www.omdbapi.com/?apikey=7c974ec7&s=' + titulo + '&type=movie')
        resposta = json.loads(req.text)
    except:
        print('Conexao falhou')
        return quant

    if resposta['Response'] == 'True':
        quant = resposta['totalResults']
    return quant

def lista_filmes(titulo):
    lista = []
    
    for i in range(1,101):
        try:
            req = requests.get('http://www.omdbapi.com/?apikey=7c974ec7&s=' + titulo + '&type=movie&page=' + str(i))
            resposta = json.loads(req.text)

            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    titulo = filme['Title']
                    ano = filme['Year']
                    lista.append(titulo + ' (' + ano + ')')
        except:
            print('Conexao falhou')

    return lista


##print(existeFilmes('matrix'))

##print(lista_filmes('matrix'))

sair = False

while not sair:
    op = raw_input('Pesquise por um filme ou digite SAIR:')
    if op.upper() == 'SAIR':
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados: ' + str(len(lista_de_filmes)))

        for filme in lista_de_filmes:
            print(filme)

