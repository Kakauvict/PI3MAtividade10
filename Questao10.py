total = 0
vendas = []

for i in range(1, 7):
    valor = float(input(f"Digite a venda do mês {i}: "))
    vendas.append(valor)
    total += valor

media = total / 6

acima_media = 0

for venda in vendas:
    if venda > media:
        acima_media += 1

print("Total de vendas:", total)
print("Média mensal:", media)
print("Meses acima da média:", acima_media)
