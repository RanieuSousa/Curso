populacao_A = 80000
taxa_crescimento_A = 0.03  # 3% de crescimento anual
populacao_B = 200000
taxa_crescimento_B = 0.015  # 1.5% de crescimento anual
anos = 0

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a população do país B.")
