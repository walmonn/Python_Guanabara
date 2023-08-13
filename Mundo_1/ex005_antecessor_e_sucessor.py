#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input("Digite um número: "))
a = n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {}, e o seu sucessor é {}" .format(n, a, s))
print("Analisando o valor {}, seu antecessor é {}, e o seu sucessor é {}" .format(n, (n-1), (n+1)))

#pode-se fazer das duas maneiras, porem o correto é fazer o codigo o mais limpo possivel, então o ideal é usar o 2º Print
