valor1 = int(input('insira o primeiro valor inteiro: '))
valor2 = int(input('insira o segundo valor inteiro: '))
fecharPrograma = False

while(fecharPrograma == False):
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior numero')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcaoEscolhida = int(input('>>>>> Sua opcao: '))

    while(opcaoEscolhida < 1 or opcaoEscolhida > 5):
        print('Essa opçao nao existe, escolha um numero de 1 a 5.')
        opcaoEscolhida = int(input('>>>>> Sua nova opcao: '))
    
    if(opcaoEscolhida == 1):
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    if(opcaoEscolhida == 2):
        print(f'{valor1} X {valor2} = {valor1 * valor2}')
    if(opcaoEscolhida == 3):
        if(valor1 > valor2):
            print(f' entre {valor1} e {valor2}, o maior numero é {valor1}')
        else:
            print(f' entre {valor1} e {valor2}, o maior numero é {valor2}')
    if(opcaoEscolhida == 4):
        valor1 = int(input('insira o primeiro valor inteiro: '))
        valor2 = int(input('insira o segundo valor inteiro: '))
    if(opcaoEscolhida == 5):
        fecharPrograma = True
    print('\n')