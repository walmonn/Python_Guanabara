# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Digite a quantidade de KM Rodados: "))
dias = int(input("Digite a quantidade de dias: "))
preco = (km * 0.15) + (dias * 60)
print(f"Você usou o carro por {dias} dias e rodou {km} KM, e irá pagar um total de R${preco:.2f} pelo aluguel do carro.")
