import math

a = input('ввести сторону а:')
b = input('ввести сторону в:')
c = input('ввести сторону с:')

a = float(a)
b = float(b)
c = float(c)

p = (a + b + c) / 2

s = math.sqrt(p*(p - a) * (p - b) * (p - c))

print('Площа трикутника = ' + str(s))