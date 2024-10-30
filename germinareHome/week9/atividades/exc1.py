import math
#definindo a quantidade de funcionarios
while True:
    try:
        quantidadeFuncionarios = int(input('Insira a quantidade de funcionarios: '))
        break
    except ValueError:
        print('Insira apenas o numero de funcionarios')

#definindo o salario total do funcionario
listaSalarial = []
listaNomes = []
for funcionario in range(quantidadeFuncionarios):
    while True:
        try:
            listaNomes.append(input(f'Insira o nome do funcionario {funcionario + 1}: '))
            valorVendasBrutas = float(input(f'\nInsira o ganho das vendas brutas de {listaNomes[funcionario]}: '))
            ganhoTotalFuncionario = 200+valorVendasBrutas*0.09
            while(valorVendasBrutas < 0):
                print('\nO valor de vendas brutas nao pode ser negativo')
                valorVendasBrutas = float(input(f'Insira o NOVO ganho das vendas brutas do funcionario {listaNomes[funcionario]}: '))
            break
        
        except ValueError:
            print('Insira apenas em numeros, um valor valido')
        
    listaSalarial.append(ganhoTotalFuncionario)
    
#definindo cada classe de salario para cada salario
listaClasseSalarial = []
for salario in listaSalarial:
    classeSalarial = math.ceil((salario-200)/100)
    listaClasseSalarial.append(classeSalarial)
    

for indice, nome in enumerate(listaNomes):
    print('-----------------------------')
    print(f'Funcionario {indice + 1}: {nome}')
    print(f'Salario Total: {listaSalarial[indice]}')
    print(f'Classe Salarial: posição {listaClasseSalarial[indice]}')