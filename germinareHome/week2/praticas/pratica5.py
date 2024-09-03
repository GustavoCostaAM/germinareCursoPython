# EXERCICIO 5 -  tabuada:
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

# feito sem copiar e/ou auxilios
numero = int(input('escreva um numero e veja sua tabuada: '))

for x in range(1, 11):
    print(f'{numero} x {x} = {numero*x}')