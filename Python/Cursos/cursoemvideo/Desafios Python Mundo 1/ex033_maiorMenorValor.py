#Exercício Python 033: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

num_a = int(input('Digite um número inteiro: '))
maior=menor=num_a
num_b = int(input('Digite outro: '))
if num_b > maior: maior=num_b
elif num_b < menor: menor=num_b
num_c = int(input('Digite mais um: '))
if num_c > maior: maior=num_c
elif num_c < menor: menor=num_c
print(f'O maior valor digitado foi {maior}\nO menor valor digitado foi {menor}')
