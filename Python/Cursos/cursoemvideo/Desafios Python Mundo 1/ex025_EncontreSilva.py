#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

filtro = 'silva'
nome = str(input('Qual o seu nome completo? ')).lower().strip()
print(f'Seu nome tem Silva? {nome.find(filtro)>=0}')
