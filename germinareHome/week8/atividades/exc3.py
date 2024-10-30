#definindo a quantiade de alunos do Tech
while True:
    try:
        alunosTech = int(input('Digite a quantidade de alunos atuais na escola Germinare Tech: '))
        while(alunosTech <= 0):
            print('Insira um valor positivo')
            alunosTech = int(input('Digite a NOVA quantidade de alunos atuais na escola Germinare Tech: '))
        break
    except ValueError:
        print('Digite um valor inteiro valido')
        
#definindo a quantidade de alunos do Bussines

while True:
    try:
        alunosBussines = int(input('Digite a quantidade de alunos atuais na escola Germinare Bussines: '))
        while(alunosBussines <= 0):
            print('Insira um valor positivo')
            alunosBussines = int(input('Digite a NOVA quantidade de alunos atuais na escola Germinare Bussines: '))
        break
    except ValueError:
        print('Digite um valor inteiro valido')
        
#verificando a quantidade de anos minimos nescessarios para o tech passar o bussines

anosPrecisos = 0
while alunosTech < alunosBussines:
    alunosBussines*=1.10
    alunosTech*=1.50
        
    anosPrecisos+=1


#saida de dados
if(anosPrecisos == 0):
    print('\nA quantidade de alunos da Germinare Tech ja é maior ou igual a do Bussines.')
else:
    print(f'\nNo total, será preciso de {anosPrecisos} ano(s) para a Germinare Tech passar da bussines')
    print(f'quantidade de alunos esperada (aproximadamente): ')
    print(f'>GERMINARE TECH: {alunosTech:.0f}')
    print(f'>GERMINARE BUSSINES: {alunosBussines:.0f}')