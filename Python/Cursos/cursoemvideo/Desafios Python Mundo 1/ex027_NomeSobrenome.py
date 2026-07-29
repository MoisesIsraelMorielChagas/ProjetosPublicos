#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente.

nomeCompleto = str(input('Digite seu nome completo: ')).title().strip()
lnomec = nomeCompleto.split() #lista nome completo
nome, sobrenome = lnomec[0], lnomec[-1]
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome}')
print(f'Seu último nome é {sobrenome}')
