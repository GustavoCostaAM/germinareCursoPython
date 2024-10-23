#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor

numeroDigitado = float(input('Digite um numero: '))
porcaoInteriaDoNumero = floor(numeroDigitado)
print(f'\nO numero digitado foi: {numeroDigitado}')
print(f'sua porcao inteira é: {porcaoInteriaDoNumero}')