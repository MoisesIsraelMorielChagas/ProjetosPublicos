#Crie um programa que receba um numero dado pelo usuário e mostre a tabuada na tela.

def linha():
    print('-'*24)

def tabuada(n, i=0, f=10):
    resultado = n*i
    print(f'{n} x {i:>2} = {resultado}')
    if i < f:
        tabuada(n, i+1, f)

numero = int(input('Digite um numero para ver sua tabuada: '))
linha()
tabuada(numero)
linha()
