#Crie um programa que mostre na tela todos os números pares que estão em um intervalo

#definindo o numero inicial
while True:
    try:
        numeroInicial = int(input('Digite o numero inicial: '))
        break
    except(ValueError):
        print('Digite apenas um numero inteiro valido\n')

#definindo o numero final

while True:
    try:
        numeroFinal = int(input('Digite o numero final: '))
        break
    except(ValueError):
        print('Digite apenas um numero inteiro valido')
        
#verificando e printando todos os numeros pares da sequencia

for numero in range(numeroInicial, numeroFinal+1):
    if(numero%2==0):
        print(f'{numero}', end=', ')