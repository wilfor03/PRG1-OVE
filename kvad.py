svar = input('skriv ett tal ')
x = float (svar)
y = x * x
print (f'talet i kvadrat är {y:.2f}')


i = 19
print (f'Resultat: {i}')
j = 107
print (f'Resultat: {j:5}')
k = 4
print (f'Resultat: {k:03}')


import math
a = float(input('första sidan? '))
b = float(input('andra sidan? '))
c = math.sqrt (a**2 + b**2)
print (f'hypotenusans längd: {c:.2f}')


import random
print('tärningen är kastad')
n = random.randint(1,6)
print('du fick', n)


pris = float(input('grundpris? '))
ålder = int(input('Ålder? '))
if ålder < 12:
    pris = pris * 0.5
else:
    pris = pris * 0.9
print(f'pris: {pris:.2f} kr')