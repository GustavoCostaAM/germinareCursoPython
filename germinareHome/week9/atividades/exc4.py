listaCarros = []
listaConsumo = []

for indiceVeiculo in range(0, 5):
    print(f'Veiculo {indiceVeiculo + 1}')
    carro = input('Insira o modelo do veiculo: ')
    while True:
        try:
            consumo = float(input('Insira o consumo (km/L) do veiculo: '))
            break
        except ValueError:
            print('Insira o consumo de km por litros EM numeros, substitua "," por "."\n')
    
    listaCarros.append(carro)
    listaConsumo.append(consumo)

#calculando litros de gasolina para andar 1000km e adicionando em uma lista
listaLitrosGasolina1000km = []
valorGasto1000km = []
for indice, carro in enumerate(listaCarros):
    consumoPara1000km = listaConsumo[indice]*1000
    valorGasto = consumoPara1000km*2.25
    
    listaLitrosGasolina1000km.append(consumoPara1000km)
    valorGasto1000km.append(valorGasto)

#fazendo a saida de dados

print(f'N | {'modelo':<20} | Consumo | Litros para 1000km | Valor de gasolina')
print('-'*75)

for indice, carro in enumerate(listaCarros):
    print(f'{indice+1} | {carro:<20} | {listaConsumo[indice]:<7.2f} | {f'{listaLitrosGasolina1000km[indice]:.2f} Litros':<18} | R${valorGasto1000km[indice]:.2f}')
    
    
print(f'O carro com menor consumo é {listaCarros[listaConsumo.index(min(listaConsumo))]}')