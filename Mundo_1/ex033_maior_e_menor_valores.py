# Faça um programa que leia três números e mostre qual é o maior e qual é o.

a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O Menor valor digitado foi {}'.format(menor))
print('O Maior Valor digitado foi {}'.format(maior))
