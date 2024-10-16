print('Mercado J&F - Promocao Friboi')
print('cardapio:')

print('1- File Duplo')
print('2- Alcatra')
print('3- Picanha')

produto = int(input('Selecione o produto que deseja comprar: '))

if(produto != 1 and produto != 2 and produto != 3):
    print(f'\033[31m Houve um erro, produto {produto} nao encontrado no sistema, desconsiderar as proximas operacoes.')
    
    
kg = float(input('Digite a quantidade, em kg, que deseja levar: '))

cartaoDebito = input('A compra sera realizada no cartao de debito? \n 1- SIM \n 2- NAO \n sua escolha: ')

if(cartaoDebito != "1" and cartaoDebito != "2"):
    print(f'\033[31m Houve um erro, opcao {cartaoDebito} nao existe, favor desconsiderar as proximas operacoes.')
    cartaoDebito = 3
elif(cartaoDebito == "1"):
    cartaoDebito = True
else:
    cartaoDebito = False
    
if(produto == 1 and kg <= 5):
    valor = 4.90
    carne = "File Duplo"
elif(produto == 1 and kg >= 5):
    valor = 5.80
    carne = "File Duplo"
elif(produto == 2 and kg <= 5):
    valor = 5.90
    carne = "Alcatra"
elif(produto == 2 and kg >= 5):
    valor = 6.80
    carne = "Alcatra"
elif(produto == 3 and kg <= 5):
    valor = 6.90
    carne = "Picanha"
elif(produto == 3 and kg >= 5):
    valor = 7.80
    carne = "Picanha"

print('**************************CUPOM FISCAL**************************')

print(f'carne: {carne}')
print(f'quantidade(kg): {kg}')
print(f'preco: {round((valor*kg),2)}')

if(cartaoDebito == True):
    print('Compra feita com cartao de debito: SIM')
    print(f'total com desconto: {round((valor*kg)-(((valor*kg)/100)*5), 2)}')
elif(cartaoDebito == False):
    print('Compra feita com cartao de debito: NAO')
    print(f'total sem descontos: {round((valor*kg), 2)}')
elif(cartaoDebito == 3):
    print('\033[31m Houve um erro ao selecionar uma das opcoes pedidas, tente novamente. \033[m')