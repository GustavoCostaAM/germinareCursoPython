numeroUsuario = int(input('Insira um numero inteiro e positivo: '))

while(numeroUsuario < 0):
    print('\ninsira apenas um unico numero inteiro e positivo!')
    numeroUsuario = int(input('novo numero: '))

todosVerificados = "Falso"
numeroPar = "Falso"
numeroPrimo = "Falso"
numeroArmstrong = "Falso"
numeroQuadradoPerfeito = "Falso"
numeroPalindromo = "Falso"
numeroTemFibonacci = "Falso"


#verificando se o numero é par
if(numeroUsuario%2 == 0):
    numeroPar = True
else:
    numeroPar = False

#verificando se o numero é primo

if(numeroUsuario%2 != 0 and numeroUsuario%3 != 0 and numeroUsuario%5 != 0):
    numeroPrimo = True
else:
    numeroPrimo = False

#verificando se o numero é de Armstrong
numeroUsuarioString = str(numeroUsuario)
contador = 0
numerosIndividual = []

while(contador < len(numeroUsuarioString)):
    numerosIndividual.append(str(numeroUsuarioString[contador]))
    contador +=1
   


resultCalculos = sum(int(digito)**len(numerosIndividual) for digito in numerosIndividual)

if(resultCalculos == numeroUsuario):
    numeroArmstrong = True
else:
    numeroArmstrong = False


#verificando se o numero é um quadrado perfeito

if(isinstance(numeroUsuario**0.5, int)):
    numeroQuadradoPerfeito = True
else:
    numeroQuadradoPerfeito = False

#veriicando se o numero é Palindromo

#criando array que recebe as mesmas informacoes do numerosIndividual, porem de forma contraria

numerosIndividualContrario = list(reversed(numerosIndividual))

if(numerosIndividual == numerosIndividualContrario and numerosIndividual[0] != 0):
    numeroPalindromo = True
else:
    numeroPalindromo = False

#definindo se o numero faz parte da sequencia de fibonacci:

listaTermos = []

termo1 = 0
termo2 = 0
termo3 = termo1 + termo2

contagem = 0

while(contagem < numeroUsuario):
    
    listaTermos.append(termo3)
    
    if(contagem == 0):
        termo2 = 1
    else:
        termo1 = termo2
        termo2 = termo3
        termo3 = termo1 + termo2
        
        
    contagem = contagem + 1
    
if(listaTermos.count(numeroUsuario)):
    numeroTemFibonacci = True
else:
    numeroTemFibonacci = False

print(numeroTemFibonacci)

#SAIDA DE DADOS:

print(f'/nEm base do numero {numeroUsuario}, aqui está algumas informaçoes sobre ele:\n')

#saida se é par ou impar
if(numeroPar == True):
    print('O numero inserido é par\n')
else:
    print('O numero inserido é impar\n')

#saida se é primo ou nao
if(numeroPrimo == True):
    print('O numero inserido é primo\n')
else:
    print('O numero inserido nao é primo\n')

#saida se é armstrong ou nao
if(numeroArmstrong == True):
    print('O numero inserido é de Armstrong\n')
else:
    print('O numero inserido nao é de Armstrong\n')

#saida se é um quadrado perfeito ou nao
if(numeroQuadradoPerfeito == True):
    print('O numero inserido é um quadrado perfeito\n')
else:
    print('O numero inserido nao é um quadrado perfeito\n')
    
#saida se é um numero palindromo
if(numeroPalindromo == True):
    print('O numero inserido é um palindromo\n')
else:
    print('O numero inserido nao é um palindromo\n')
    
#saida se o numero faz parte da sequencia de fibonacci
if(numeroTemFibonacci == True):
    print('O numero inserido faz parte da sequencia de fibonacci\n')
else:
    print('O numero inserido nao faz parte da sequencia de fibonacci\n')