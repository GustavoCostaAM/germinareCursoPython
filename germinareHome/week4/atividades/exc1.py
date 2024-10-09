valorSaque = int(input('Insira o valor desejado para o saque: '))
while(valorSaque < 10 or valorSaque > 600):
    valorSaque = int(input('Erro, insira uma quantia entre R$10,00 e R$600,00: '))
    
notasDeCem = valorSaque // 100
notasDeCinquenta = (valorSaque%100)//50
notasDeDez = ((valorSaque%100)%50)//10
notasDeCinco = (((valorSaque%100)%50)%10)//5
notasDeDois = ((((valorSaque%100)%50)%10)%5)//2

print(f'notas de cem: {notasDeCem}')
print(f'notas de cinquenta: {notasDeCinquenta}')
print(f'notas de dez: {notasDeDez}')
print(f'notas de cinco: {notasDeCinco}')
print(f'notas de dois: {notasDeDois}')