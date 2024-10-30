listaIdades = []

#armazenando todas as idades na lista listaIdades
for numero in range(1, 81):
    #input da idade
    while True:
        try:
            idade = int(input(f'Para a pessoa {numero}, digite sua idade: '))
            while(idade<0):
                print('insira uma idade positiva')
                idade = int(input(f'Para a pessoa {numero}, digite sua NOVA idade: '))
            
            break
        except ValueError:
            print('Insira uma idade valida, apenas com numeros.')
    #adicionando a idade na lista
    listaIdades.append(idade)

#tratamento de dados
idadeMedia = sum(listaIdades)/len(listaIdades)
maiorIdade = max(listaIdades)
menorIdade = min(listaIdades)

#faixas etarias
quantidadeBebes = 0
quantidadeCriancas = 0
quantidadePreAdolescente = 0
quantidadeAdolescentes = 0
quantidadeJovens = 0
quantidadeAdultos = 0
quantidadeIdosos = 0

for idade in listaIdades:
    if(idade < 2):
        quantidadeBebes +=1
    elif(2 <= idade < 10):
        quantidadeCriancas+=1
    elif(10 <= idade < 14):
        quantidadePreAdolescente+=1
    elif(14 <= idade < 18):
        quantidadeAdolescentes+=1
    elif(18 <= idade < 21):
        quantidadeJovens+=1
    elif(21 <= idade < 60):
        quantidadeAdultos+=1
    else:
        quantidadeIdosos+=1
        
#SAIDA DE DADOS

print(f'\nA idade media foi de {idadeMedia:.2f} anos')
print(f'A menor idade foi: {menorIdade}')
print(f'A maior idade foi: {maiorIdade}')

print('\nQuantidade de pessoas em cada faixa etária: \n')

print(f'Bebê: {quantidadeBebes}')
print(f'Criança: {quantidadeCriancas}')
print(f'Pré-adolescente: {quantidadePreAdolescente}')
print(f'Adolescente: {quantidadeAdolescentes}')
print(f'Jovem: {quantidadeJovens}')
print(f'Adulto: {quantidadeAdultos}')
print(f'Idoso: {quantidadeIdosos}')