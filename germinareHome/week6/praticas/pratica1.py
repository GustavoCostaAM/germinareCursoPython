numeroDigitado = input('Insira um numero: ')
numeros = [numeroDigitado[numero] for numero in range(len(numeroDigitado))]

numeros = list(reversed(numeros))

unidades = numeros[0]
dezenas = numeros[1]
centenas = numeros[2]
milhares = numeros[3]

print(f'\nO numero digirado tem:\n')
print(f'{unidades} unidades')
print(f'{dezenas} dezenas')
print(f'{centenas} centenas')
print(f'{milhares} milhares')