import time

#definindo o tempo de minutos para a contagem
while True:
    try:
        minutosIniciais = int(input('Insira o tempo em minutos da contagem regressiva: '))
        while(minutosIniciais < 0):
            print('insira um valor inteiro positivo ou 0')
            minutosIniciais = int(input('Insira o NOVO tempo em minutos da contagem regressiva: '))
        break
    except ValueError:
        print('Insira um valor em numeros')

#se o tempo de minutos for 0, entao definindo os segundos
if(minutosIniciais == 0):
    while True:
        try:
            segundosIniciais = int(input('Insira entao, o tempo em segundos da contagem regressiva: '))
            while(not 0<=segundosIniciais<60):
                print('insira um valor inteiro positivo, menor que 60')
                segundosIniciais = int(input('Insira o NOVO tempo em segundos da contagem regressiva: '))
            break
        except ValueError:
            print('Insira um valor em numeros')

#realizando a contagem regressiva

#definindo os minutos e segundos atuais
minutosAtuais = minutosIniciais
try:
    segundosAtuais = segundosIniciais
except NameError:
    segundosAtuais = 0

while True:
    if(minutosAtuais == 0 and segundosAtuais <= 10):
        print('\033[31m', end='')
    print(f'{minutosAtuais:02}:{segundosAtuais:02}')
    
    if(minutosAtuais == 0 and segundosAtuais == 0):
        print('\033[m')
        break
    
    if(segundosAtuais == 0):
        minutosAtuais -=1
        segundosAtuais = 60
    
    segundosAtuais -=1
    time.sleep(1)