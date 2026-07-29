#Crie um programa que pergunte ao professor o nome de 4 alunos, escolha um aluno e
#mostre ao professor.

from random import choice

indagacao= 'Primeiro aluno: '

alunos = [str(input(indagacao)),
          str(input(indagacao.replace('Primeiro', 'Segundo'))),
          str(input(indagacao.replace('Primeiro', 'Terceiro'))),
          str(input(indagacao.replace('Primeiro', 'Quarto')))]

print(f'O aluno escolhido foi {choice(alunos)}.')
