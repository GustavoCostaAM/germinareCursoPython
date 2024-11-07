import datetime
import time

def calcularSegundos():
    
    horaAtual = datetime.datetime.now().hour
    minutoAtual = datetime.datetime.now().minute
    segundoAtual = datetime.datetime.now().second

    segundosPassados = segundoAtual+(minutoAtual*60)+((horaAtual*60)*60)
    segundosRestantes = 86400 - segundosPassados
    
    print(f'\nSegundos passados: {segundosPassados}')
    print(f'Segundos restantes: {segundosRestantes}')
    

horaAtual = datetime.datetime.now().hour
minutoAtual = datetime.datetime.now().minute
segundoAtual = datetime.datetime.now().second

while True:
    calcularSegundos()
    time.sleep(60)