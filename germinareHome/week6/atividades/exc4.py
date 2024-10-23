novoCliente = True
listaValoresProdutos = []


while(True):
    #definindo a quantidade de produtos e seus preços
    produtosQuantidade = 0
    contadorWhile = 0
    while(True):
        #criando novos produtos, pedindo ao usuario os valores, e adicionando em listas e incrementando em variaveis
        adicionarNovoProduto = str(input('Deseja adicionar um novo produto? digite S/N: ')).strip().lower()
        while(adicionarNovoProduto != 's' and adicionarNovoProduto != 'n'):
            print('essa opcao nao existe, digite apenas S/N')
            adicionarNovoProduto = input('nova resposta: ').strip().lower()
       
        #condicionando a adicionar um novo valor ou a parar o sistema
        if(adicionarNovoProduto == 's'):
            produtosQuantidade +=1
            valorProduto = float(input(f'Insira o valor do produto {produtosQuantidade}: R$'))
            while(valorProduto <=0):
                print('Insira um valor que seja maior que 0')
                valorProduto = float(input('insira o novo valor: R$'))
            listaValoresProdutos.append(valorProduto)
        elif(adicionarNovoProduto == 'n'):
            break
   
   
    #definindo descontos e saida de dados
    if(produtosQuantidade < 2):
        percentualDesconto = 0
    elif(2<=produtosQuantidade<=4):
        percentualDesconto = 5
    elif(5<=produtosQuantidade<=7):
        percentualDesconto = 10
    elif(produtosQuantidade>8):
        percentualDesconto = 15
   
    valorTotalSemDescontos = sum(listaValoresProdutos)
    valorDesconto = valorTotalSemDescontos*(percentualDesconto/100)
    valorTotalComDescontos = valorTotalSemDescontos - valorDesconto
   
    print('\n---------------------RELATORIO FINAL---------------------')
    print(f'Valor parcial: R${valorTotalSemDescontos:.2f}')
    print(f'Desconto atingindo: {percentualDesconto}% | R${valorDesconto:.2f}')
    print(f'Valor Total: R${valorTotalComDescontos:.2f}')
       
       
    novoCliente = input('\nTem algum outro cliente na fila? Responda S/N: ').strip().lower()
    while(novoCliente != 's' and novoCliente != 'n'):
        print('essa opcao nao existe, responda apenas S/N')
        novoCliente = input('nova resposta: ').strip().lower()
   
    if(novoCliente == 'n'):
        print('\nEncerrando caixa...')
        break