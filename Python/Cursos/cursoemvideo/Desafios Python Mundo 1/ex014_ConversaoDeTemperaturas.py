#Crie um programa que receba uma temperatura em graus Celsius (°C)
# converta para Fahrenheit (ºF) e mostre na tela.

temp_celsius = float(input('Informe a temperatura ºC: '))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f'A temperatura de {temp_celsius:.1f}ºC corresponde a {temp_fahrenheit:.1f}ºF!')
