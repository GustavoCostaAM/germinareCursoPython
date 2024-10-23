numeros = input('insira tres diferentes numeros, os separando por espaço: ').split()

numeros = [int(numero) for numero in numeros]

numeros = sorted(numeros)

print(f'Menor numero: {numeros[0]} \nMaior numero: {numeros[2]}')
print(f'numeros em ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}')