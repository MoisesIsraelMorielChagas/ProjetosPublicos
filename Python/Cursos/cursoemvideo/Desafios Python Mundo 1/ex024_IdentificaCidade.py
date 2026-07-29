#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a
#palavra "Santo".

filtro = 'SANTO'
cidade = str(input('Em que cidade você nasceu? ')).upper().strip()
print(cidade[:5] == filtro)
