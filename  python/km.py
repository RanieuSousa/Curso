# Solicita ao usuário a distância em quilômetros e a velocidade média em km/h
distancia_em_km = float(input("Digite a distância em quilômetros: "))
velocidade_media_em_kmph = float(input("Digite a velocidade média em km/h: "))

# Calcula o tempo em horas
tempo_em_horas = distancia_em_km / velocidade_media_em_kmph

# Converte o tempo em horas para horas, minutos e segundos
horas = int(tempo_em_horas)
minutos = int((tempo_em_horas - horas) * 60)
segundos = int(((tempo_em_horas - horas) * 60 - minutos) * 60)

# Imprime o resultado
print(f"Tempo estimado de viagem: {horas} horas, {minutos} minutos e {segundos} segundos.")
