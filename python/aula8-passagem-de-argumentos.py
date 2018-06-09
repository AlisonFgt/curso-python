import sys

# arg1 metod // arg2 - n1 // arg3 - n2
argumentos = sys.argv

#print(argumentos)

def soma(n1,n2):
    return float(n1) + float(n2)

def sub(n1,n2):
    return float(n1) - float(n2)

if argumentos[1] == 'soma':
    resp = soma(argumentos[2], argumentos[3])
elif argumentos[1] == 'sub':
    resp = sub(argumentos[2], argumentos[3])

print(resp)