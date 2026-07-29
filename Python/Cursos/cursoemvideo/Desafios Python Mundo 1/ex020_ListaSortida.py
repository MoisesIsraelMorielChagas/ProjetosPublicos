#Crie um programa que receba o nome de 4 alunos e mostre na tela uma lista em ordem
#aleatória, indicando a ordem de quem apresentará o trabalho primeiro.

from random import shuffle

faluno = 'aluno: '
fpAluno = f'Primeiro {faluno}'
fsAluno = f'Segundo {faluno}'
ftAluno = f'Terceiro {faluno}'
fqAluno = f'Quarto {faluno}'

alunos = [str(input(fpAluno)),
          str(input(fsAluno)),
          str(input(ftAluno)),
          str(input(fqAluno))]

shuffle(alunos) #Sorteando alunos
print(f'A ordem de apresentação será\n{alunos}')
