#input do valor do imovel
while True:
    try:
        valorImovel = float(input('Insira o valor do imovel: '))
        break
    except ValueError:
        print('Insira um valor valido')
        
#input e tratamento de dados do valor do investimento mensal
while True:
    try:
        investimentoMensal = float(input('Insira o valor do investimento mensal: '))
        break
    except ValueError:
        print('Insira um valor valido')

while(investimentoMensal < valorImovel*0.01):
    print('O valor do investimento é menor que 1% do valor do imovel, é inviavel realizar esse investimento.')
    while True:
        try:
            investimentoMensal = float(input('\nInsira o NOVO valor do investimento mensal: '))
            break
        except ValueError:
            print('Insira um valor valido')
            
#input da taxa mensal de juros
while True:
    try:
        taxaMensalJuros = float(input('Insira o valor da taxa mensal de juros (em %): '))
        break
    except ValueError:
        print('\nInsira um valor valido, tente apenas digitando o valor')
        
#calculando os messes nescessarios e a saida de dados
meses = 0
investimentoAtual = investimentoMensal
while True:
    if(investimentoAtual >= valorImovel):
        print(f'De acordo com os dados fornecidos, é preciso de {meses} meses no minimo para poder pagar o imovel, e irá sobrar R${investimentoAtual - valorImovel:.2f} extras.')
        break
    
    investimentoAtual = (investimentoAtual*(1 + taxaMensalJuros/100))+investimentoMensal
    
    meses+=1