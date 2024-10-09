#definindo o gabarito base da prova
gabaritoProva = input('Voce deseja usar o gabarito padrão ou adicionar um novo? digite PADRAO ou NOVO: ').strip().lower()
acertosTurma = []
alunosTotais = 0
while(gabaritoProva != 'padrao' and gabaritoProva != 'novo'):
    print('Essa opcao nao existe, digite apenas PADRAO ou NOVO')
    gabaritoProva = input('Nova resposta: ').strip().lower()

if(gabaritoProva == 'padrao'):
    gabaritoProva = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
else:
    print('digite o gabarito correto com 10 respostas, com apenas um espaco entre uma alternativa e outra')
    gabaritoProva = input('Insira o gabarito: ').upper().split()
    while(0<len(gabaritoProva)<10):
        print('A quantidade de alternativas nao esta dentro do intervalo de 1 até 10, tente novamente.')
        gabaritoProva = input('Insira o gabarito: ').upper().split()



#definindo o gabarito do aluno, quantidade de acertos e incrementando para a lista de acertos da turma

while(True):
    #definindo o gabarito do aluno
    print('Insira o gabarito do aluno, com espaco entre uma alternativa e outra')
    gabaritoAluno = input('Gabarito do aluno: ').upper().split()
    alunosTotais +=1
   
    #definindo a quantidade de acertos do aluno
    contadorWhile = 0
    numeroAcertos = 0
    while(contadorWhile < 10):
        if(gabaritoAluno[contadorWhile] == gabaritoProva[contadorWhile]):
            numeroAcertos +=1
       
        #colocando o numero de acertos para os acertos da turma
        contadorWhile +=1
       
    acertosTurma.append(numeroAcertos)
    
    continuar = input('Deseja parar o programa ou continuar com outro aluno? responda PARAR ou CONTINUAR: ').strip().lower()
   
    if(continuar == 'parar'):
        break
   
mediaTurma = numeroAcertos/alunosTotais

print('\n----------------------RELATORIO FINAL----------------------')
print(f'\nNo total, {alunosTotais} aluno/s utilizaram o sistema')
print(f'A media da turma foi de {mediaTurma:.1f} acertos')
print(f'A maior nota foi {max(acertosTurma)}, e a nota menor foi de {min(acertosTurma)}')