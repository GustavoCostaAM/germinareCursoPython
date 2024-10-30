import math

#Definindo a hora de entrada
horaEntradaInput = input('digite a hora de entrada do veiculo (formato: hora h minuto): ')

#loop para que a hora de entrada esteja com a formatacao correta
while(len(horaEntradaInput) > 5 or "h" not in horaEntradaInput):
   print('Houve um problema em um dos dados inseridos, tente novamente, com a formatacao correta')
   horaEntradaInput = input('digite a hora de entrada do veiculo (formato: hora h minuto): ')
   
entrada = horaEntradaInput.split("h",2)

#definindo hora de saida

horaSaidaInput = input('digite a hora de saida do veiculo (formato: hora h minuto): ')

#loop para que a hora de saida esteja com a formatacao correta
while(len(horaSaidaInput) > 5 or "h" not in horaSaidaInput):
   print('Houve um problema em um dos dados inseridos, tente novamente, com a formatacao correta')
   horaSaidaInput = input('digite a hora de saida do veiculo (formato: hora h minuto): ')

saida = horaSaidaInput.split("h",2)

#definindo o tempo que o veiculo ficou no estacionamento

hoursToPay = 0
if(int(entrada[0]) > int(saida[0])):
    hoursToPay = (24 - int(entrada[0])+ int(saida[0]))
    if(int(entrada[1]) > 0):
        hoursToPay = hoursToPay + 1
    if(int(saida[1]) > 0):
        hoursToPay = hoursToPay + 1
elif(int(saida[0]) > int(entrada[0])):
    hoursToPay = int(saida[0]) - int(entrada[0])
    if(int(entrada[1]) > 0):
        hoursToPay = hoursToPay + 1
    if(int(saida[1]) > 0):
        hoursToPay = hoursToPay + 1
        
        
#definindo o valor que sera pago
valorTotal = 0
if(hoursToPay == 1 or hoursToPay == 2):
    valorTotal = hoursToPay
elif(hoursToPay == 3 or hoursToPay == 4):
    valorTotal = 2 + 1.40*2
elif(hoursToPay >= 5):
    valorTotal = (2 + 1.40*2) + 2*(hoursToPay-4)
    

print(f'horas a serem cobradas: {hoursToPay}')
print(f'Valor total do estacionamento: R${valorTotal:.2f}')