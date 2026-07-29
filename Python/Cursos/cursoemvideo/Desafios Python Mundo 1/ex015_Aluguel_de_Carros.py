#Crie um programa que calcule o preço do aluguel de um carro baseado nos fatores abaixo:
#Quantos Dias foi alugado o carro?
#Quantos Km o alugador percorreu com o carro no periodo alugado?
#O carro deve custar R$ 60,00 por dia e R$0.15 por Km Rodado.

dias_alugados = int(input('Quantos dias Alugados: '))
km_rodado = float(input('Quantos Km rodados: '))
aluguel = (dias_alugados*60) + (km_rodado*0.15)
print(f'O total a pagar é de R${aluguel}')
