#Desenvolva um programa que pergunte a distancia de uma viagem em Km e...
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para passagens ate 200Km.
#e R$ 0,45 para viagens mais longas.

d = float(input('Qual é a distância da sua viagem? '))
preco = 0.50*d if (d<=200) else 0.45*d
print(f'Você está prestes a começar uma viagem de {d:.1f}Km.')
print(f'E o preço da sua passagem será R${preco:.2f}')
