#Escreva um programa que leia a velocidade de um carro.
#Se exceder 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa deve custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'''\033[91mMULTADO! Você excedeu o limite permitido que é 80Km/h
Você deve pagar uma multa de \033[93mR${multa:.2f}!\033[m''')
print('\033[92mTenha um bom dia! Dirija com segurança!\033[m')
