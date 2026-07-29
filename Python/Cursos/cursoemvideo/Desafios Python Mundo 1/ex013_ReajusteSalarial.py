#Crie um programa que receba do financeiro a quantidade de reais de um funcionário e
#retorne o valor simulado do salário + aumento de 15%.

salario_func = float(input('Qual é o salário do Funcionário? R$'))
percentual_de_aumento = 0.15
novo_salario_func = salario_func * (1.0 + percentual_de_aumento)
print(f'Um funcionário que ganhava R${salario_func:.2f},'
      f' com 15% de aumento, passa a receber R${novo_salario_func:.2f}')
