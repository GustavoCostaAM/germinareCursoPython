import random
print('-----' * 10)
print('irei pensar em um numero de 1 a 5, voce tem que tentar advinhar')
print('-----' * 10)

numeroEscolhido = int(input('insira seu numero: '))
numeroPensado = random.randint(1,5)

if(numeroPensado == numeroEscolhido):
    print(f'voce pensou em {numeroEscolhido}, eu também.')
else:
    print(f'Eu ganhei! voce pensou em {numeroEscolhido}, eu pensei em {numeroPensado}')