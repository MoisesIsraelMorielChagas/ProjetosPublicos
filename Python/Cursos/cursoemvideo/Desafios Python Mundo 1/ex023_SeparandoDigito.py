#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos
# digitos separados.

num = str(input('Informe um numero: ')) #número
numf = f'{num:0>4}' #numero formatado.
milhar = numf[0]
centena = numf[1]
dezena = numf[2]
unidade = numf[3]
print(f'Analisando o numero {num[:4]}')
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
