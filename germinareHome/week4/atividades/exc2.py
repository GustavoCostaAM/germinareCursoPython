velocidadeMaxima = float(input('Insira a quantidade maxima permitida na via, em km/h: '))
velocidadeVeiculo = float(input('Insira a velocidade do veiculo no momento da infraçao: '))

if(velocidadeMaxima >= velocidadeVeiculo):
    print('O veiculo estava dentro dos limites, nenhuma sansão será aplicada')
elif(velocidadeVeiculo <= velocidadeMaxima*1.2):
    print('O veiculo esteve até 20% da velocidade maxima permitida, multa de R$130,00 deverá ser aplicada')
elif(velocidadeVeiculo > velocidadeMaxima*1.2 and velocidadeVeiculo <= velocidadeMaxima*1.5):
    print('O veiculo esteve entre 20% até 50% da velocidade maxima permitida, multa de R$200,00 deverá ser aplicada')
else:
    print('O veiculo ultrapassou de 50% a mais da velocidade maxima permitida na via, multa de R$500,00 e suspensão da habilitação')