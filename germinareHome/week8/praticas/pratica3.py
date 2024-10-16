#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

dataAtual = datetime.date.today()
anoAtual = dataAtual.year

#input dos anos de nascimento
listaAnosDeNascimento = []
for numero in range(1, 8):
    while True:
        try:
            anoNascimento = int(input(f'Para a pessoa {numero}, digite seu ano de nascimento: '))
            
            while(anoNascimento > anoAtual):
                print(f'O ano de nascimento nao pode ser maior que o ano atual({anoAtual})')
                anoNascimento = int(input(f'Para a pessoa {numero}, digite seu ano de nascimento: '))
            
            break
        except(ValueError):
            print('Digite apenas o ano, em numeros inteiros e validos')
           
    listaAnosDeNascimento.append(anoNascimento)

#verificando a quantidade de idades maior ou igual a 18
contadorIdadesMaior = 0
for nascimento in listaAnosDeNascimento:
    idade = anoAtual - nascimento
    if(idade >= 18):
        contadorIdadesMaior +=1
        
contadorIdadesMenor = 7-contadorIdadesMaior

#saida de dados

print(f'\nAo todo, tiveram {contadorIdadesMaior} pessoas de maior de idade, e {contadorIdadesMenor} de menor de idade.')