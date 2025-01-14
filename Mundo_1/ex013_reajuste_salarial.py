# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario_atual = float(input("Digite o seu salário: R$ "))
aumento = salario_atual + (salario_atual * 15 / 100)
print(f"O seu salário atual de {salario_atual:.2f} após um aumento de 15% passará a ser de {aumento:.2f}")
