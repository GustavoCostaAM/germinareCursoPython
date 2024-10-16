from random import shuffle

listaNomes = input('Digite o nume de cada pessoa, com um espaco de distancia para separar: ').strip().split()
shuffle(listaNomes)
print(f'A ordem sorteada é: {listaNomes}')