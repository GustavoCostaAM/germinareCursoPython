from random import randint

perguntas = 0
valorA = randint(1, 20)
valorB = randint(1, 20)
acertos = 0

for perguntas in range(0,5):
    valorA = randint(1, 20)
    valorB = randint(1, 20)
    resposta = int(input(f'Pergunta: {valorA} X {valorB} = '))
    if(resposta == valorA*valorB):
        acertos = acertos + 1
        print('Acertou')
        print(f'respostas corretas: {acertos}\n')
    else:
        print('Errou')
        print(f'A resposta correta era {valorA*valorB}')
        print(f'respostas corretas: {acertos} \n')