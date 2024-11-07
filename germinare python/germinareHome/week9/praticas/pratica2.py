import random

numerosStorteados = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), )

for numeros in numerosStorteados:
    print(numeros, end=', ')

print(f'\nO maior numero sorteado foi: {max(numerosStorteados)}')
print(f'O menor numero sorteado foi: {min(numerosStorteados)}')