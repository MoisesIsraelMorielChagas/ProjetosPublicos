#Faça um programa que leia um angulo qualquer e mostre na tela:
#o valor do seno, cosseno e tangente desse angulo.

from math import  radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
anguloR = radians(angulo)
seno = sin(anguloR)
cosseno = cos(anguloR)
tangente = tan(anguloR)

print(f'''O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}
O ângulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}
O ângulo de {angulo:.1f} tem a TANGENTE de {tangente:.2f}
''')
