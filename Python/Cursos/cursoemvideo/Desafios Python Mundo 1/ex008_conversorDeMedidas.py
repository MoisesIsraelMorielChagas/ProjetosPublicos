#Crie um programa que receba do usuário uma distancia (m) e mostre esta distancia em:
# km ; hm ; dam ; dm ; cm ; mm.

dist_m = float(input('Uma distancia em metros: '))
km = dist_m / 1000; hm = dist_m / 100; dam = dist_m / 10
dm = dist_m * 10; cm = dist_m * 100; mm = dist_m * 1000
print(f'''A medida de {dist_m}m corresponde a
{km}km
{hm}hm
{dam}dam
{dm:.0f}dm
{cm:.0f}cm
{mm:.0f}mm
''')
