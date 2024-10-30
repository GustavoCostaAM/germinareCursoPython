numero1 = int(input('insira o numero 1: '))
numero2 = int(input('insira o numero 2: '))
numero3 = int(input('insira o numero 3: '))
print('\n')

#definindo e printando o maior numero
if(numero1 > numero2 and numero1 > numero3):
    print(f'o numero {numero1} é o maior')
elif(numero2 > numero3 and numero2 > numero1):
    print(f'o maior numero é {numero2}')
else:
    print(f'o maior numero é {numero3}')

#definindo e printando o menor numero
if(numero1 < numero2 and numero1 < numero3):
    print(f'o menor numero é {numero1}')
elif(numero2 < numero1 and numero2 < numero3):
    print(f'o menor numero é {numero2}')
else:
    print(f'o menor numero é {numero3}')