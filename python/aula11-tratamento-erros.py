import time 
from datetime import datetime

def abre_arquivo():
    try:
        arquivo = open('curso-python/arquivodoido.txt')
        return True
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False


while not abre_arquivo():
    agora = datetime.now()
    print('Tentando abrir o arquivo ' + str(agora))
    time.sleep(3)

print('Consegui abrir o arquivo!')

