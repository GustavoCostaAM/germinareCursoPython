import random

saldo = 100

while(True):
    dado1 = random.randint(0,6)
    daddo2 = random.randint(0,6)
    somaDados = dado1 + daddo2
    
    valorApostado = int(input(f'\nSabendo que seu saldo atual é de {saldo}, insira a quantia que deseja apostar: '))
    
    while(valorApostado > saldo):
        print(f'Voce nao pode apostar um valor superior ao seu saldo')
        valorApostado = int(input(f'Insira o novo valor da aposta: '))
    
    if(somaDados == 7 or somaDados == 11):
        saldo += 2*valorApostado
        print(f'A soma dos dados deu {somaDados}, seu novo saldo é de {saldo}')
    else:
        saldo -= 20
        print(f'A soma dos dados deu {somaDados}, seu novo saldo é de {saldo}')
        
    if(saldo <= 0):
        break