distance = float(input('insira a distancia da viagem: '))
print(f'voce esta prestes a começar uma viagem de {distance}km')

if(distance <= 200):
    price = distance*0.50
else:
    price = distance*0.45
print(f'o valor da viagem será de R${price:.2f}')