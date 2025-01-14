# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input("Digite um numero: "))
print(f"O Numero digitado foi {num} e a parte inteira desse numero é {trunc(num)}")
