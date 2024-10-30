horasInput = int(input('Insira as horas: '))
minutosInput = int(input('Insira as os minutos: '))

def calcular_minutos_dia(horas, minutos):
    minutosAtuais = horas*60+minutos
    minutosRestantes = 1440-minutosAtuais
   
    return minutosAtuais, minutosRestantes
   
minutosAtuais, minutosRestantes = calcular_minutos_dia(horasInput, minutosInput)

print(f'até agora ja se passaram {minutosAtuais} minutos, e faltam {minutosRestantes} minutos para o fim do dia')
