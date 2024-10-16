# EXERCICIO 3 -  Média Aritmética:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# feito sem copiar e/ou auxilios

nota1 = float(input("Primeira nota: "))
nota2 = float(input("segunda nota: "))

def calcularMedia(nota1, nota2):
    return((nota1 + nota2)/2)

print(f'A media entre {nota1} e {nota2} é: {calcularMedia(nota1, nota2)}')
