import random
opcoes = ["Pedra", "Papel", "Tesoura"]
opcaoPlayer = int(input('Digite: \n 0 para jogar Pedra\n 1 para jogar papel\n 2 para jogar tesoura\nSua jogada: '))

while(opcaoPlayer > 2):
    print('houve um erro, selecione apenas 1, 2 ou 3')
    opcaoPlayer = int(input('opcao: '))

jogadaBot = random.choice(opcoes)
jogadaPlayer = opcoes[opcaoPlayer]

print(f'\na opcao que o jogador escolheu foi {jogadaPlayer}')
print(f'a opcao que o bot escolheu foi {jogadaBot}\n')

if(jogadaBot == opcoes[0] == jogadaPlayer or jogadaBot == opcoes[1] == jogadaPlayer or jogadaBot == opcoes[2] == jogadaPlayer):
    print('O jogo deu empate!')
elif(jogadaPlayer == opcoes[0] and jogadaBot == opcoes[1]):
    print('vitoria do BOT!!!!')
elif(jogadaPlayer == opcoes[1] and jogadaBot == opcoes[0]):
    print('vitoria do JOGADOR!!!!')
elif(jogadaPlayer == opcoes[1] and jogadaBot == opcoes[2]):
    print('vitoria do BOT!!!!')
elif(jogadaPlayer == opcoes[2] and jogadaBot == opcoes[1]):
    print('vitoria do JOGADOR!!!!')
elif(jogadaPlayer == opcoes[2] and jogadaBot == opcoes[0]):
    print('vitoria do BOT!!!!')
elif(jogadaPlayer == opcoes[0] and jogadaBot == opcoes[2]):
    print('vitoria do JOGADOR!!!!')