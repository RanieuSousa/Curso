
num_alunos = 5
medias = []
aprovados = 0
for i in range(num_alunos):
    print(f"Aluno {i + 1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7.0:
        aprovados += 1
print("Médias dos alunos:", medias)
print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")
