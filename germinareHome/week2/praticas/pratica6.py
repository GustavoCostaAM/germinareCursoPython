# EXERCICIO 6 -  pintando parede:
#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# feito sem copiar e/ou auxilios

altura = float(input('altura da parede em metros: '))
largura = float(input('largura da parede em metros: '))
area = altura * largura

print(f'sabendo que a altura da parede é de {altura}m, e sua largura é de {largura}m, entao, sua area é de {area}m². Para pintar essa parede, é preciso de {area/2} litros de tinta.')