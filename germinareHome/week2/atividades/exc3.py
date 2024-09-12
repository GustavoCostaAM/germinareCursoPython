#Uma empresa tem para um determinado funcionário os seguintes dados:
#a. nome do funcionário;
#b. número de horas que ele trabalha por semana;
#c. número de dependentes.
#Considere que a empresa paga R$ 25,00 por hora e R$ 500.00 por dependente. Faça um programa que imprima o nome do funcionário e o seu salário mensal. Considere que um mês tem quatro semanas.

#mais detalhes na area do curso preparatorio

nome = input('Qual o nome do funcionario? \n')
cargaHoraria = int(input(f'quantas horas {nome} trabalha por semana? \n'))
dependentes = int(input(f'quantos dependentes {nome} tem? \n'))


def calcularSalario(cargaHoraria, dependentes):
    return ((25*cargaHoraria)*4)+(500*dependentes)

print(f'{nome} terá um salario mensal de R${calcularSalario(cargaHoraria, dependentes)}')