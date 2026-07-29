#Ex35: Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

def cabecario(linha='-', tl=10, texto=''):
    print(linha*tl)
    print(texto)
    print(linha*tl)

resposta={True:'PODEM', False:'NÃO PODEM'}
cabecario(linha='-=', tl=20, texto='Analisador de Triângulos')
seg1= float(input('Primeiro Segmento: '))
seg2= float(input('Segundo Segmento: '))
seg3= float(input('Terceiro Segmento: '))
triangular= True if (seg1+seg2>seg3 and seg2+seg3>seg1 and seg3+seg1>seg2) else False
print(f'Os segmentos acima {resposta[triangular]} FORMAR um triângulo!')
