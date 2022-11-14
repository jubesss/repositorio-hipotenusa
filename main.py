nome = input('qual seu nome? ')
print('Olá',(nome),',','responda as perguntas abaixo! ')
from math import hypot
co = float (input ('comprimento do cateto oposto '))
ca = float(input('comprimento do cateto adjacente '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {}'.format(hi))
