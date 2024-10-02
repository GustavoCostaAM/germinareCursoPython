#Escreva um programa para calcular a quantidade de latas de tintas que devem ser compradas para pintar o piso de um quintal retangular, cujas dimensões são fornecidas pelo usuário. Devese calcular também o custo total para comprar as latas de tintas necessárias.

#Informações adicionais:
# Cada lata de tinta contém 5 litros
# Cada litro de tinta pinta 3 metros quadrados
# valor lata de tinta: 120R$

largura = input('Insira a largura do piso em metros: ')
comprimento = input('Insira o comprimento do piso em metros: ')

def calcular(largura, comprimento):
    area = int(largura) * int(comprimento)
    litrosDeTinta = area/3
    latasDeTinta = round(litrosDeTinta/5)
    custoTotal = latasDeTinta*120
    
    print(f'em um piso cuja largura é {largura}m, e comprimento é {comprimento}m, é nescessario comprar {latasDeTinta} latas de tinta, o custo total será de {custoTotal}R$')
    
calcular(largura, comprimento)