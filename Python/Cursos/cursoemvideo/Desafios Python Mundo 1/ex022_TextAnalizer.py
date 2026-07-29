#Crie um programa que receba do usuário o nome completo e retorne prints que informem:
#O nome em maiusculas, em minusculas, quantidade de caracteres e filtre o primeiro nome

nome_completo = str(input('Digite seu nome completo: ')).strip() #nome completo

#Analisando nome...
partes_nc = nome_completo.split() #partes do nome completo.
nome_completo_sc = ''.join(partes_nc) #nome completo sem espaços.
primeiro_nome = partes_nc[0]
qtd_car_nc = len(nome_completo_sc) #Quantidade de caracteres do nome completo.
qtd_car_pn = len(primeiro_nome)#Quantidade de caracteres do primeiro nome.

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome_completo.upper()}')
print(f'Seu nome em minúsculas é {nome_completo.lower()}')
print(f'Seu nome tem ao todo {qtd_car_nc} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {qtd_car_pn} letras')
