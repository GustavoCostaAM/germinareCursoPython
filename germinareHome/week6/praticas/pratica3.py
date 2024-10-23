fraseDigitada = input('Digite uma frase: ').strip().lower()

quantidadeDeA = fraseDigitada.count('a')
primeiroA = fraseDigitada.find('a')
ultimoA = fraseDigitada.rfind('a')

print(f'\nA frase inserida:\n')

print(f'repete a letra "a" em minusculas ou maiusculas {quantidadeDeA} vezes')
print(f'o primeiro "a" é a letra {primeiroA + 1}')
print(f'o ultimo "a" é a letra {ultimoA + 1}')