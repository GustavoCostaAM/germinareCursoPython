dicionario_Aluno = {}
dicionario_Aluno['Nome'] = input('Insira o nome do aluno: ')
dicionario_Aluno['Media'] = float(input(f'Insira a media de {dicionario_Aluno['Nome']}: '))
dicionario_Aluno['Situacao'] = 'Aprovado' if dicionario_Aluno['Media'] > 7 else 'Reprovado'


print(f'Nome do aluno: {dicionario_Aluno['Nome']}')
print(f'A media e de: {dicionario_Aluno['Media']}')
print(f'Situaçao: {dicionario_Aluno['Situacao']}')