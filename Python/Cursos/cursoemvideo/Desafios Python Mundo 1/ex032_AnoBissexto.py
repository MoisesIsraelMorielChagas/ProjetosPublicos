#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano_atual = int(date.today().year)
ano_selecionado = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
ano_selecionado = ano_selecionado if (ano_selecionado != 0) else ano_atual
bissexto = 'não é BISSEXTO'
if (ano_selecionado % 4 == 0):
    if (ano_selecionado % 400 == 0) or (ano_selecionado % 100 != 0):
        bissexto = 'é BISSEXTO'

print(f'O ano {ano_selecionado} {bissexto}')
