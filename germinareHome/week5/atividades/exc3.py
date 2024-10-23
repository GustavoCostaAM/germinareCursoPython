numeroDigitado = int(input('Digite um numero inteiro: '))
encerrarPrograma = False

#condicionando o programa para caso o usuario digitar um numero negativo, vai automaticamente encerrar o programa
if(numeroDigitado < 0):
    encerrarPrograma = True


while(encerrarPrograma == False):
    
    #colocando um intervalo de 0 até o numero digitado em um array
    listaNumeros = [0]
    numeroDefaut = 1

    while(listaNumeros[-1] < numeroDigitado):
        listaNumeros.append(numeroDefaut)
        numeroDefaut += 1
    
    
    #calculando a quantidade de numeros impares existentes

    numeroDefaut = 0
    numerosImpares = 0
    while(numeroDefaut < numeroDigitado):
        if(listaNumeros[numeroDefaut]%2 != 0):
            numerosImpares += 1
        numeroDefaut += 1
    
    
    
    
    print(f'\n No intervalo entre 1 e {numeroDigitado}, existem {numerosImpares} numeros impares\n')

    
    numeroDigitado = int(input('Digite um numero inteiro: '))
    
    if(numeroDigitado < 0):
        encerrarPrograma = True
    
print('\nNumero negativo detectado...')
print('desligando sistema\n')