#Basicamente mesmo que o exc4.py da week 6, de forma aprimoriada

#Inserindo o preco de cada produto
while True:
    try:
        quantidadeProdutos = int(input('Digite a quantidade de produtos que deseja comprar: '))
        while(quantidadeProdutos <= 0):
            print('Insira um valor positivo')
            quantidadeProdutos = int(input('Digite a NOVA quantidade de produtos que deseja comprar: '))
        break
    except ValueError:
        print('\nInsira um valor valido')

listaValoresProdutos = []

for produto in range(1, quantidadeProdutos+1):
    while True:
        try:
            valor = float(input(f'Digite o valor do produto {produto}: '))
            while(valor <= 0):
                print('Insira um valor positivo')
                valor = float(input(f'Digite o NOVO valor do produto {produto}: '))
            break
        except ValueError:
            print('\nInsira um valor valido')
    
    listaValoresProdutos.append(valor)

#tratamento de dados

valorTotalSemDescontos = sum(listaValoresProdutos)
PercentualdescontoAplicado = 0
if(valorTotalSemDescontos >= 100):
    if(quantidadeProdutos == 4):
        PercentualdescontoAplicado = 0.04
    elif(quantidadeProdutos == 5):
        PercentualdescontoAplicado = 0.08
    elif(quantidadeProdutos >= 6):
        PercentualdescontoAplicado = 0.12

valorTotalComDescontos = valorTotalSemDescontos-valorTotalSemDescontos*PercentualdescontoAplicado 
descontoAplicado = valorTotalSemDescontos*PercentualdescontoAplicado

#saida de dados

print('\n---------------------NOTA FISCAL---------------------\n')
print(f'Valor parcial: R${valorTotalSemDescontos:.2f}')
print(f'Percentual de desconto atingido: {PercentualdescontoAplicado*100}%')
print(f'Desconto total atingido: R${descontoAplicado:.2f}')
print(f'\nVALOR TOTAL: R${valorTotalComDescontos:.2f}')