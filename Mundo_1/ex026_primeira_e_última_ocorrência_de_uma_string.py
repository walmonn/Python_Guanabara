# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A Letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira Letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#Foi usado o +1 na linha 5 e 6 para eliminar o zero e começar a contar as letras a partir do 1.
