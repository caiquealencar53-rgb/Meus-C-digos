from math import hypot
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = hypot(co,ca)
print('O resultado é {:.2f}'.format(hi))