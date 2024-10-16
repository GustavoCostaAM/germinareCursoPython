import datetime

percentualAumento = 0
dataAtual = []

data = str(datetime.date.today()).split('-', 3)

salario = float(input('Insira o salario inicial do funcionario: '))

while(salario < 1000):
    print('O programa aceita apenas salarios acima de R$1000.00')
    salario = float(input('Insira o novo salario do funcionario: '))
    

anoInicial = int(input('Insira o ano inicial do funcionario na empresa: '))

while(anoInicial < 1995 or anoInicial > int(data[0])):
    print(f'O programa aceita apenas anos de inicio entre 1995 e {data[0]}.')
    anoInicial = int(input('Insira o novo ano de inicio na empresa: '))

#definindo o aumento do primeiro ano
percentualAumento = 0.015
salario += salario*percentualAumento

#proximos aumentos
diferecaAnos = int(data[0]) - anoInicial
contagem = 0
while(contagem < diferecaAnos):
    salario += salario * percentualAumento
    contagem += 1
    percentualAumento *= 1.1

percentualAumento *= 100

print(f'Percentual de aumento: {percentualAumento:.2f}%')

print(f'Salario final: R${salario:.2f}')