#Ex 34:  Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_f = float(input('Qual é o salário do funcionário? R$'))
aumento = 0.10 if (salario_f>1250) else 0.15
novo_salario = salario_f * (1+aumento)
print(f'Quem ganhava R${salario_f:.2f} passa a ganhar R${novo_salario:.2f} agora.')
