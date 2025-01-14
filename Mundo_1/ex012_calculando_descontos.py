# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input("Digite o Preço do Produto: R$ "))
desconto = (preco_produto * 5) / 100
preco_com_desconto = preco_produto - desconto
print(f"O Produto que custava {preco_produto:.2f} após um desconto de 5%, passou a valer {preco_com_desconto:.2f}")
