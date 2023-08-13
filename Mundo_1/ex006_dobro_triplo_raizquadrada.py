#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O Dobro de {} vale {}.'.format(n, d))
print('O Triplo de {} vale {}.'.format(n, t))
print('A Raiz Quadrada de {} vale {:.2f}.'.format(n, r))
