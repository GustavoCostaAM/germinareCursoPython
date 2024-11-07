palavra = (input('Digite uma palavra: '))

print(f'Na palavra {palavra}, temos: ', end=' ')

for letras in palavra:
    if('a' == letras.lower()):
        print('a', end=' ')
    elif('e' == letras.lower()):
        print('e', end=' ')
    elif('i' == letras.lower()):
        print('i', end=' ')
    elif('o' == letras.lower()):
        print('o', end=' ')
    elif('u' == letras.lower()):
        print('u', end=' ')