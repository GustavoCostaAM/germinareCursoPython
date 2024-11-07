saldoInicial = []
def compra(conta, valorCompra):
   
    saldoInicial.append(conta['saldo'])
   
    conta['transações']+=1
    conta['saldo']-=valorCompra
    conta['media']= (saldoInicial[0]-conta['saldo'])/conta['transações']

#TESTANDO A FUNCAO

conta = conta = {'transações':0, 'saldo':1000, 'media':0}

compra(conta,100)
compra(conta,200)

print(conta)