listaCanditados = []

#adicionando novos canditados e adicionando em um dicionario
contador = 1
while True:
    listaCanditados.append(dict())
    print(f'\ncanditado {contador}')
    listaCanditados[contador-1]['nome'] = input('Digite o nome: ')

    while True:
        try:
            listaCanditados[contador-1]['notaProvaTecnica'] = float(input('Insira a nota da prova tecnica: '))

            if(0<=listaCanditados[contador-1]['notaProvaTecnica'] < 11):
                break


            print('Insira um valor positivo entre 0 e 10')

        except ValueError:
            print('Insira um valor numerico')

    while True:
        try:
            listaCanditados[contador-1]['notaRedacao'] = float(input('Insira a nota da redacao: '))

            if(0<=listaCanditados[contador-1]['notaRedacao'] < 11):
                break


            print('Insira um valor positivo entre 0 e 10')

        except ValueError:
            print('Insira um valor numerico')

    while True:
        try:
            listaCanditados[contador-1]['tempoExperiencia'] = float(input('Insira o tempo de experiencia: '))

            if(0<listaCanditados[contador-1]['tempoExperiencia']):
                break


            print('Insira um valor positivo maior que 0')

        except ValueError:
            print('Insira um valor numerico')

    while True:
        try:
            maisCanditado = int(input('Tem mais canditado? 1 para sim e 2 para nao: '))

            if(1<=maisCanditado<=2):
                break


            print('Insira um valor positivo entre 1 e 2')

        except ValueError:
            print('Insira um valor numerico')


    if(maisCanditado == 2):
        break

    contador+=1


#calculando as medias

for canditado in listaCanditados:
    media = (canditado['notaProvaTecnica']+canditado['notaRedacao'])/2

    canditado['media'] = media

    if(canditado['tempoExperiencia'] < 3):
        canditado['notaFinal'] = media * 1.1
    elif(3<=canditado['tempoExperiencia']<=5):
        canditado['notaFinal'] = media * 1.3
    else:
        canditado['notaFinal'] = media * 1.5


#saida de dados nota final
print('\nResultados:\n')
for canditado in listaCanditados:
    print(f'{canditado['nome']} - pontuacao final: {canditado['notaFinal']:.2f}')
