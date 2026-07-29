#Crie um programa que calcule quantos litros de tinta serão necessários para pintar uma parede.
#Leve em consideração:
#O usuario deve informar a largura e altura da parede;
#Sabendo que 1 Litro de tinta pinta 2m² da parede.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area_P = largura * altura
litros_tinta = area_P / 2
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area_P}m².')
print(f'Para pintar esta parede, você precisará de {litros_tinta}L de tinta.')
