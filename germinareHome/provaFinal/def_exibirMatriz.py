#FUNCAO DE EXIBIR MATRIZ
def exibir_matriz(matriz):
    for valor in range(len(matriz)):
        print(f'{matriz[valor][0]} {matriz[valor][1]} {matriz[valor][2]}')