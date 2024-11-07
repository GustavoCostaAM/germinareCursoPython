import random
import math

numeroA = random.randint(0,20)
numeroB = random.randint(0,20)

def calcularFatorial(numeroA, numeroB):
    fatorialNumeroA = math.factorial(numeroA)
    fatorialNumeroB = math.factorial(numeroB)
   
    return fatorialNumeroA + fatorialNumeroB

soma_fatorial_n_A_B = calcularFatorial(numeroA, numeroB)

print(f'Numero A: {numeroA}')
print(f'Numero B: {numeroB}')
print(f'Resultado da soma dos fatoriais: {soma_fatorial_n_A_B}')