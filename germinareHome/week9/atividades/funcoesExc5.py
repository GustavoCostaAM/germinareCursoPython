#FUNCAO DE EXIBIR MATRIZ
def exibir_matriz(matriz):
    for valor in range(len(matriz)):
        print(f'{matriz[valor][0]} {matriz[valor][1]} {matriz[valor][2]}')





#FUNCAO DE VERIFICAR VENCEDOR
def verificar_vencedor(matriz):
    coordenadasX = []
    coordenadasO = []
    resultado = None
    #pegando todas as coordenadas de X e de Y
    for indiceLinha in range(len(matriz)):
        for indiceColuna in range(len(matriz[indiceLinha])):
            valor = matriz[indiceLinha][indiceColuna]
            if(valor == 'X'):
                coordenadasX.append([indiceLinha, indiceColuna])
            elif(valor == 'O'):
                coordenadasO.append([indiceLinha, indiceColuna])
            
            
            
    
    #TODAS POSSIBILIDADES POSSIVEIS PARA 1 VENCER
    
    if(all(coordenada in coordenadasX for coordenada in [[0, 0], [0, 1], [0, 2]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[1, 0], [1, 1], [1, 2]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[2, 0], [2, 1], [2, 2]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[0, 0], [1, 0], [2, 0]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[0, 1], [1, 1], [2, 1]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[0, 2], [1, 2], [2, 2]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[0, 0], [1, 1], [2, 2]])):
        resultado = 'Jogador 1 venceu'
    elif(all(coordenada in coordenadasX for coordenada in [[0, 2], [1, 1], [2, 0]])):
        resultado = 'Jogador 1 venceu'
    
    
    #TODAS POSSIBILIDADES POSSIVEIS PARA 2 VENCER
    
    if(all(coordenada in coordenadasO for coordenada in [[0, 0], [0, 1], [0, 2]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[1, 0], [1, 1], [1, 2]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[2, 0], [2, 1], [2, 2]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[0, 0], [1, 0], [2, 0]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[0, 1], [1, 1], [2, 1]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[0, 2], [1, 2], [2, 2]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[0, 0], [1, 1], [2, 2]])):
        resultado = 'Jogador 2 venceu'
    elif(all(coordenada in coordenadasO for coordenada in [[0, 2], [1, 1], [2, 0]])):
        resultado = 'Jogador 2 venceu'
    
    #VERIFICANDO CASOS DE EMPATE 
    linhasCompletas = []
    for indice, linha in enumerate(matriz):
        if('-' not in linha):
            linhasCompletas.append(indice)
    
    if(all(valor in linhasCompletas for valor in [0, 1, 2]) and resultado != 'Jogador 1' and resultado != 'Jogador 2'):
        resultado = 'empate'
    
    return resultado