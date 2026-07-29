#Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça ao
#usuário para tentar adivinhar qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('\033[93m-=\033[m'*60)
print('\033[94mVou pensar em um numero entre 0 e 5. Tente adivinhar...\033[m')
print('\033[93m-=\033[m'*60)
pensamento_pc = randint(0, 5)
resposta = int(input('Em que número pensei? '))
print('\033[95mPROCESSANDO...\033[m')
sleep(2)
if pensamento_pc == resposta:
    print('\033[92mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[91mGANHEI! Eu pensei no número {pensamento_pc} e não no {resposta}!\033[m')
