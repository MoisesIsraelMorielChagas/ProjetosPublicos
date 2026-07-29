#Crie um programa que receba um dado numérico de um usuário e mostre na tela:
#O dobro, o triplo e a raiz quadrada deste numero.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'O dobro de {numero} vale {dobro}.')
print(f'O triplo de {numero} vale {triplo}.')
print(f'A raiz quadrada de {numero} é igual a {raiz:.2f}.')
