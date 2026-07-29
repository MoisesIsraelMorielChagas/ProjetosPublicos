#Dissecando Variaveis

var_x = input('Digite algo: ')
tp_x = type(var_x) #tipo primitivo variavel x
print(f'O tipo primitivo desse valor é: {tp_x}')
print(f'Só tem espaços? {var_x.isspace()}')
print(f'É um número? {var_x.isnumeric()}')
print(f'É alfabético? {var_x.isalpha()}')
print(f'É alfanumérico? {var_x.isalnum()}')
print(f'Esta em maiúsculas? {var_x.isupper()}')
print(f'Esta em minúsculas? {var_x.islower()}')
print(f'Esta capitalizada? {var_x.istitle()}')
print(f'É um valor ascii? {var_x.isascii()}')
print(f'É um dígito? {var_x.isdigit()}')
print(f'É um decimal? {var_x.isdecimal()}')
print(f'Pode ser impresso? {var_x.isprintable()}')
print(f'É um identificador? {var_x.isidentifier()}')




                                                            #Ass: Moisés Israel Moriel Chagas