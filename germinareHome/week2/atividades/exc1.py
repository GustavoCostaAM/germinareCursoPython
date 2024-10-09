exc = input('Qual exercicio deseja ver? digite 1 para ver o primeior, e 2 para o segundo: ')

if (exc == "1"):
    #PARTE 1]
    
    # Escreva um programa que converta um intervalo de tempo, dado em segundos, para horas, minutos e segundos. Por exemplo, se o tempo dado for de 3850 ‘segundos’, o algoritmo deve fornecer como resultado 1h 4min 10s, nesse formato
    
    segundos = int(input('Digite a quantidade de segundos: '))
    
    def calcular1(seconds):
        seg = (seconds%3600)%60
        min = (seconds%3600)//60
        hr = seconds//3600
        
        print(f'{hr}h, {min}m, {seg}s')
    
    calcular1(segundos)
else:
    #PARTE 2
    
    #Agora inverta, faça com que o usuário digite uma hora, e retorne quantos segundos tem esse horário, por exemplo, se o dado de entrada for: 1:04:10, deve retornar como saída 3850 segundos.
    
    horaCompleta = input('Digite uma hora: ')
    
    def calcular2(horaCompleta):
        horarios = horaCompleta.split(":", 3)
        hr = int(horarios[0])
        min = int(horarios[1])
        seg = int(horarios[2])
        
        segTotais = (hr*3600)+seg + (min*60)
        print(segTotais, ' segundos')
    
    calcular2(horaCompleta)