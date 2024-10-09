valorSaque = int(input('Insira o valor desejado para o saque: '))
while(valorSaque <= 0):
    valorSaque = int(input('Erro, insira uma quantia pelo menos equivalente a R$1'))


notasDeCinquenta = valorSaque//50
notasDeDez = (valorSaque%50)//10
notasDeUm = ((valorSaque%50)%10)

print(f'notas de cinquenta: {notasDeCinquenta}')
print(f'notas de dez: {notasDeDez}')
print(f'notas de um: {notasDeUm}')