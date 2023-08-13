#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input("Digite alguma coisa: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços ?", a.isspace())
print("É um numero ?", a.isnumeric())
print("É alfabetico ?", a.isalpha())
print("É alfanumerico ?", a.isalnum())
print("Está em letras minusculas ?", a.islower())
print("Ésta em letras maiusculas ?", a.isupper())
print("Está capitalizada ?", a.istitle())
