cliente1 = int(input('Qual a idade do primeira cliente? '))
cliente2 = int(input('Qual a idade do seguna cliente? '))

#calculando o valor total pelo cliente 1
if(cliente1 <= 17):
    valorPrimeiroCliente = 15
elif(cliente1 >= 18 and cliente1 <= 59):
    valorPrimeiroCliente = 30
else:
    valorPrimeiroCliente = 20

#calculando o valor total pelo  cliente 2

if(cliente2 <= 17):
    valorSegundoCliente = 15
elif(cliente2 >= 18 and cliente2 <= 59):
    valorSegundoCliente = 30
else:
    valorSegundoCliente = 20
    
print(f'Valor a ser cobrado pelo primeiro cliente: R${valorPrimeiroCliente}')
print(f'Valor a ser cobrado pelo segundo cliente: R${valorSegundoCliente}')

print(f'\nTotal a ser cobrado: R${(valorSegundoCliente + valorPrimeiroCliente):.2f}')