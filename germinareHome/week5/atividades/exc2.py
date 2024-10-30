from random import randint

nivelDificuldade = input('Selecione um nivel de dificulade: facil, medio ou dificil \n sua resposta: ').lower()
numeroBot = 0
    
while(nivelDificuldade != 'facil' and nivelDificuldade != 'medio' and nivelDificuldade != 'dificil'):
    print(f'opçao "{nivelDificuldade}" nao existe, selecione apenas facil, medio ou dificil')
    nivelDificuldade = input('nova resposta: ').lower()
    print(' ')


if(nivelDificuldade == 'facil'):
    numeroBot = randint(0, 10)
    print('Dificuldade facil ativada, apenas numeros entre 0 e 10 \n')
elif(nivelDificuldade == 'medio'):
    numeroBot = randint(0, 50)
    print('Dificuldade medio ativada, apenas numeros entre 0 e 50 \n')
else:
    numeroBot = randint(0, 100)
    print('Dificuldade dificil ativada, apenas numeros entre 0 e 100 \n')


numeroTentativas = 0
usuarioAcertou = False

while(usuarioAcertou == False):
    numeroPlayer = int(input('Tente acertar o numero que pensei: '))
    if(numeroPlayer > numeroBot):
        print('O numero digitado é maior \n')
    elif(numeroPlayer < numeroBot):
        print('O numero digitado é menor \n')
    else:
        usuarioAcertou = True
    
    numeroTentativas += 1
print(f'Parabens voce acertou!!! foram precisas {numeroTentativas} tentativas')