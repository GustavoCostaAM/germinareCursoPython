import random

numeroUsuario = int(input('Digite um numero: '))
palpiteUsuario = input('vai dar par ou impar(P/I): ').strip().upper()

while(palpiteUsuario != "P" and palpiteUsuario != "I"):
    print(f'{palpiteUsuario} nao existe, escreva apenas P ou I')
    palpiteUsuario = input('novo palpite: ').strip().upper()

numeroBot = random.randint(0, 10)

total = numeroBot + numeroUsuario

print(f'Voce digitou {numeroUsuario}, ja o bot digitou {numeroBot}')
print(f'O total foi de {total}, ou seja, ', end='')

if(total%2 == 0):
    print(f'a soma é par\n')
    if(palpiteUsuario == "P"):
        print('Voce venceu!!!')
    else:
        print('Voce perdeu... Tente novamente')
else:
    print(f'a soma é impar\n')
    if(palpiteUsuario == "I"):
        print('Voce venceu!!!')
    else:
        print('Voce perdeu... Tente novamente')