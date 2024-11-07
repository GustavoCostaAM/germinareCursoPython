# EXERCICIO 1 -  Dissecando uma Variável:
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

variavel = input('Me diga algo: ')
print('tipo primitivo: ', type(variavel))
print('so tem espacos: ', variavel.isspace())
print('e um numero: ', variavel.isalnum())
print('e alfabetico: ', variavel.isalpha())
print('e alfanumerico: ', variavel.isalnum())
print('esta em maiuscula: ', variavel.isupper())
print('esta em minuscula: ', variavel.islower())
print('esta capitalizada: ', variavel.istitle()) #feito em base de comentarios do video