# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO'.format(ano))
else:
    print('O Ano {} não é BISSEXTO'.format(ano))
    