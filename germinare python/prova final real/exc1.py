def calcular_divida(valorEmprestimo, acrescimo):
    return valorEmprestimo+(valorEmprestimo*acrescimo/100)

def calcular_parcela(valorFinal, quantidadeMeses):
    return valorFinal/quantidadeMeses

#ENTRADA DE INFORMACAO

while True:
    try:
        valorEmprestimo = float(input('Insira o valor do emprestimo: R$'))
        if(0<valorEmprestimo):
            break

        print('Insira um valor de emprestimo positivo')
    except ValueError:
        print('insira um valor numerico')

while True:
    try:
        acrescimo = int(input('Insira o percentual de acrescimo (em %): '))
        if(acrescimo > 0):
            break

        print('Insira um valor numerico inteiro positivo')

    except ValueError:
        print('Insira um valor numerico inteiro')


while True:
    try:
        meses = int(input('Em quantos meses voce vai pagar a divida: '))
        if(meses>0):
            break

        print('Insira os meses acima de 0')
    except ValueError:
        print('insira um valor numerico positivo inteiro')


valorDividaTotal = calcular_divida(valorEmprestimo, acrescimo)
parcelasMensais = calcular_parcela(valorDividaTotal, meses)



#SAIDA DE DADOS

print('\nResumo do emprestimo')

print(f'valor solicitado: R${valorEmprestimo}')
print(f'taxa de acrescimo: {acrescimo}%')
print(f'quantidade de meses: {meses}')
print(f'divida total: {valorDividaTotal:.2f}')
print(f'parcelas mensais: {parcelasMensais}')