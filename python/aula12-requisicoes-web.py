import requests
#Beautiful Soup 4 BS4 pip install bs4

cabecalho = {'User-agent':  'Linux 22',
             'Referer':     'https://google.com',
             'CF_IPcountry':'US'}

meus_cookies = {'Ultima-visita': '10-10-2020'}

dados = {'username': 'alisonfgt',
         'password': 'ali123123'}

texto = None

try:
    #requisicao = requests.get('https://putsreq.com/lFx54ZRlOJMQ8NYDes5j')
    requisicao = requests.post('https://putsreq.com/lFx54ZRlOJMQ8NYDes5j', 
                                headers = cabecalho,
                                cookies = meus_cookies,
                                data = dados)
    texto = requisicao.text
except Exception as e:
    print('Requisição deu erro: ', e)

print(texto)