# EXERCICIO 4 -  Conversor de Medidas:
#Escreva um programa que leia um valor em metros e o exiba convertido em outras medidas

# feito sem copiar e/ou auxilios
medida = float(input('medida em metros: '))
print(f'a distancia de {medida} metros pode ser convertida para:')
print(f'{medida/1000} km')
print(f'{medida/100} hm')
print(f'{medida/10} dam')
print(f'{medida*10} dm')
print(f'{medida*100} cm')
print(f'{medida*1000} mm')