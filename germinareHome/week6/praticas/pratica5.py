sexo = input('Insira seu sexo M/F: ').strip().upper()
while(sexo != "M" and sexo != "F"):
    print(f' sexo {sexo} nao existe')
    sexo = input('Insira seu sexo M/F: ').upper()
print(f'\nsexo {sexo} registrado com sucesso.')