# EXERCICIO 7 -  Calculando Descontos:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input('valor do produto: '))
desconto = valorProduto-(valorProduto/100*5)
print(f'Um produto que custa {valorProduto} reais, com 5% de desconto fica por {round(desconto, 2)} reais.')