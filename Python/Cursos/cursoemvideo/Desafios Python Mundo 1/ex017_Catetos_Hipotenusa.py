#Crie um programa que calcule a hipotenusa de um triangulo retangulo.
#O programa deve receber do usuario o Cateto Oposto e o Adjacente também,
#A partir da obtenção dos dados requeridos acima, o programa calculará
# e mostrará na tela a hipotenusa.
#Utilize a importação de módulos.

from math import hypot

catop = float(input('Comprimento do cateto oposto: ')) #cateto oposto
catad = float(input('Comprimento do cateto adjacente: ')) #cateto adjacente
hipotenusa = hypot(catop, catad)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
