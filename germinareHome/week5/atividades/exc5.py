#definindo as primeiras iniciais
valorDivida = float(input('Insira o valor da divida: '))
valorPagarMensalmente = float(input('insira o valor que o cliente deseja pagar mensalmente:'))
dividaPaga = False

if(valorPagarMensalmente == valorDivida):
    dividaPaga = True
    print('\nO valor que o cliente pagara mensalmente e igual ao valor da divida, com isso, o cliente precisa apenas fazer um pagamento unico.')
elif(valorPagarMensalmente > valorDivida):
    valorExtornado = valorPagarMensalmente - valorDivida
    print(f'\nO valor a pagar mensalmente supera o valor da divida, com isso, após o pagamento será extornado R${valorExtornado}.')
else:
    quantidadeDeMes = round(valorDivida/valorPagarMensalmente)
    contagem = 0
    valorRestante = valorDivida
    
    print(f'\nO cliente terá que pagar o valor de R${valorPagarMensalmente:.2f} durante {quantidadeDeMes} messes.\n')
    
    while(dividaPaga == False and contagem < quantidadeDeMes):
        contagem += 1
        print(f'\nMES {contagem}')
        print(f'----------------------------------------------------------------------')
        print(f'\nValor da divida de antes: {valorRestante}')
        valorRestante = valorRestante - valorPagarMensalmente
        print(f'Novo valor da divida: {valorRestante}')
        
        
        if(contagem == quantidadeDeMes):
            dividaPaga = True
        
    valorTotalPago = quantidadeDeMes*valorPagarMensalmente
    valorDiferenca = valorTotalPago - valorDivida
    if(valorTotalPago > valorDivida):
        print(f'\nHouve uma desigualdade na quantidade de mes, o cliente pagou R${valorDiferenca:.2f} a mais, esse valor será extornado ao cliente.')