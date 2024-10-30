#criando uma funcao para exibir uma matriz
from funcoesExc5 import exibir_matriz, verificar_vencedor

#criando uma matriz 3x3
matrizCampo = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
movimentosTotais = 0
while True:
    
    #definindo o movimento do jogador 1 sem possibilidades de erro
    while True:
        print('\033[31mJOGADOR 1:\033[m')
        
        #fazendo print do campo(matriz)
        exibir_matriz(matrizCampo)
        
        try:
            linha = int(input('Insira a linha: '))-1
            
            while(not 0<=linha<3):
                print('\nInsira uma linha entre 1 e 3')
                linha = int(input('Insira a NOVA linha: '))
            
            coluna = int(input('insira a coluna: '))-1
            
            while(not 0<=coluna<3):
                print('\nInsira uma coluna entre 1 e 3')
                coluna = int(input('Insira a NOVA coluna: '))
                
                
            if(matrizCampo[linha][coluna] != '-'):
                print('Essa posiçao ja esta oucupada, tente novamente...\n')
            else:
                matrizCampo[linha][coluna] = 'X'
                movimentosTotais+=1
                break
            
        except ValueError:
            print('\nInsira um valor numerico inteiro positivo entre 1 e 3\n')
    
    result = verificar_vencedor(matrizCampo)
    if(result != None):
        print('\nFIM DE JOGO')
        exibir_matriz(matrizCampo)
        print('\n')
        break
    
    
    #definindo o movimento do jogador 2 sem possibilidades de erro
    while True:
        print('\033[32mJOGADOR 2:\033[m')
        
        #fazendo print do campo(matriz)
        exibir_matriz(matrizCampo)
        
        try:
            linha = int(input('Insira a linha: '))-1
            
            while(not 0<=linha<3):
                print('\nInsira uma linha entre 1 e 3')
                linha = int(input('Insira a NOVA linha: '))
            
            coluna = int(input('insira a coluna: '))-1
            
            while(not 0<=coluna<3):
                print('\nInsira uma coluna entre 1 e 3')
                coluna = int(input('Insira a NOVA coluna: '))
                
                
            if(matrizCampo[linha][coluna] != '-'):
                print('Essa posiçao ja esta oucupada, tente novamente...\n')
            else:
                matrizCampo[linha][coluna] = 'O'
                movimentosTotais+=1
                break
            
        except ValueError:
            print('\nInsira um valor numerico inteiro positivo entre 1 e 3\n')
    
    result = verificar_vencedor(matrizCampo)
    if(result != None):
        print('\nFIM DE JOGO')
        exibir_matriz(matrizCampo)
        print('\n')
        break
        
print(f'{result} após {movimentosTotais} rodadas')
    