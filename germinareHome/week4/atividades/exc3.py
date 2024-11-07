#Crie um programa que o usuário vai digitar 3 números inteiros quaisquer e ele deve informar qual o maior e o menor desses 3 números. No final, mostre os 3 números em ordem crescente. 

numeros = input('insira tres diferentes numeros, os separando por espaço: ').split()

numeros[0] = int(numeros[0])
numeros[1] = int(numeros[1])
numeros[2] = int(numeros[2])

if(numeros[0] > numeros[1] and numeros[0] > numeros[2]):
    maiorNumero = numeros[0]
    if(numeros[1] > numeros[2]):
        menorNumero = numeros[2]
        meioNumero = numeros[1]
    else:
        menorNumero = numeros[1]
        meioNumero = numeros[2]
elif(numeros[1] > numeros[2] and numeros[1] > numeros[0]):
    maiorNumero = numeros[1]
    if(numeros[0] > numeros[2]):
        menorNumero = numeros[2]
        meioNumero = numeros[0]
    else:
        menorNumero = numeros[0]
        meioNumero = numeros[2]
else:
    maiorNumero = numeros[2]
    if(numeros[1] > numeros[0]):
        menorNumero = numeros[0]
        meioNumero = numeros[1]
    else:
        menorNumero = numeros[1]
        meioNumero = numeros[0]
        
print(f' O maior numero é: {maiorNumero}\n ja o menor numero é: {menorNumero}')
print(f'numeros em ordem crescente: {menorNumero}, {meioNumero}, {maiorNumero}')