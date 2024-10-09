termos = int(input('Quantos termos voce deseja ver? ')) + 1
contagem = 0

termo1 = 0
termo2 = 0
termo3 = termo1 + termo2

listaTermos = []

while(contagem < termos):
    
    listaTermos.append(termo3)
    
    if(contagem == 0):
        termo2 = 1
    else:
        termo1 = termo2
        termo2 = termo3
        termo3 = termo1 + termo2
        
        
    contagem = contagem + 1

del listaTermos[0]

print(f'{listaTermos}')