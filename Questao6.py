total = 0
maior_consumo = 0
produto_maior = 0

for i in range(1, 8):
    consumo = float(input(f"Digite o consumo do produto {i}: "))

    total += consumo

    if consumo > maior_consumo:
        maior_consumo = consumo
        produto_maior = i

print("Consumo total:", total, "kg")
print("Produto com maior consumo:", produto_maior)
print("Maior consumo:", maior_consumo, "kg")
