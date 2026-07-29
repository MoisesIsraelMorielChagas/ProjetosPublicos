#Crie um programa que receba um valor em reais e mostre na tela:
# quantos dolares você pode comprar.

reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dollars = reais / 5.43
print(f'Com R${reais:.2f} você pode comprar US${dollars:.2f}')

#OBS: No dia 01/10/2024, às 20:45hs da noite, o Dollar estava custando R$5,43.
