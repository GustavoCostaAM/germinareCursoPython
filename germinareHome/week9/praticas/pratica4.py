listaValores = []

while True: 
    
    novoNumero = int(input('Insira um valor: '))
    
    if(novoNumero not in listaValores):
        listaValores.append(novoNumero)
        print('valor adicionado com sucesso...\n')
    else:
        print('Valor duplicado, nao irei adicionar...\n')
    
    desejaContinuar = input('Deseja continuar? S/N: ')
    
    if(desejaContinuar == 'N'):
        break
    
print('Encerrando programa...')