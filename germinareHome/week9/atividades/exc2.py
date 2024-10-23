#definindo a quantidade de alunos totais na sala
while True:
    try:
        alunosTotais = int(input('Insira a quantidade de alunos na sala: '))
        break
    except ValueError:
        print('Insira um numero inteiro\n')

#definindo as notas(primeira e segunda) de cada aluno em uma lista juntamente com o nome

listaNomesAlunos = []
notasAlunos = []

for aluno in range(alunosTotais):
    nomeAluno = input(f'\nInsira o nome do aluno {aluno + 1}: ')
    listaNomesAlunos.append(nomeAluno)
    
    
    while True:
        #inserindo a primeira nota do aluno de acordo com o indice
        try:
            primeiraNota = float(input(f'Insira a primeira nota de {nomeAluno}: '))
            segundaNota = float(input(f'Insira a segunda nota de {nomeAluno}: '))
            
            notasAlunos.append(primeiraNota)
            notasAlunos.append(segundaNota)
            break
        except ValueError:
            print('insira apenas numeros\n')


#processando as medias das notas de cada aluno

media = []
quantidadeNotasBaixas = 0

for indiceNota in range(0, len(notasAlunos), 2):
    media.append((notasAlunos[indiceNota]+notasAlunos[indiceNota+1])/2)

print(f'{'N:':<5}    {'aluno':<15}    {'Nota1':<10}    {'Nota2':<10}    {'Media':<5}    Conceito:')

for indice, nome in enumerate(listaNomesAlunos):
    print(f'{indice+1:<5}    {nome:<15}    {notasAlunos[indice*2]:<10}   {notasAlunos[indice*2+1]:<10}    {media[indice]:<5.2f}', end=' ')
    if(media[indice] < 7):
        print('       Reprovado\n')
    else:
        print('       aprovado\n')
    
    if(media[indice] < 7):
        quantidadeNotasBaixas+=1

mediaTurma = sum(notasAlunos)/len(notasAlunos)

print(f'Media da turma: {mediaTurma:.2f}')
print(f'No total de {len(listaNomesAlunos)} alunos, {quantidadeNotasBaixas} deles ficaram com uma media final a baixo de 7')