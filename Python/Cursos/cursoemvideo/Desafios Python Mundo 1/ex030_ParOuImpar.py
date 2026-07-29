#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Impar.

n = int(input('\033[35mMe diga um número qualquer: \033[m'))
imparPar = '\033[34mPAR\033[m' if (n%2==0) else '\033[34mÍMPAR\033[m'
print(f'O número {n} é {imparPar}')
