#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram em um intervalo

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
        

#colocando todos os numeros multiplos de 3 em uma lista

listaMultiplosDe3 = []

for numero in range(numeroInicial, numeroFinal + 1):
    if(numero%2!=0):
        if(numero%3==0):
            listaMultiplosDe3.append(numero)
print(f'A soma de todos os multiplos de 3 dentro do intervalo solicitado é: {sum(listaMultiplosDe3)}')