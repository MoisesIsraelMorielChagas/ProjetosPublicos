#Crie um programa que receba o preço de um produto,
#Calcule o desconto do preço total deste mesmo produto e mostre na tela a diferença entre
#o valor inicial e o valor com desconto.
#Nota: O desconto deverá ser de 5%.

preco_inicial = float(input('Qual é o preço inicial do produto? R$'))
preco_final = preco_inicial - (preco_inicial* 0.05)
print(f'O produto que custava R${preco_inicial:.2f}, na promoção com desconto de 5% vai custar R${preco_final:.2f}')
