## Crie um programa que receba um numero inteiro e mostre na tela o numero digitado e
# a sua parte inteira separadamente. Ex: Você digitou 2.345 e sua parte inteira é 2.

import math

num_qualquer = float(input('Digite um número: '))
int_nq = math.trunc(num_qualquer)
print(f'O número {num_qualquer} tem a parte inteira {int_nq}.')
