#Crie um programa que receba 2 notas de um aluno, calcule a média e mostre o resultado na tela.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'A média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}')
