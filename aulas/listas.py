frutas = ["Limão", "Banana", "Uva", "Pitaya"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Ariel", 20, True, "Programador"]

for dado in dados:
    print(f"dado {dado}")

alunos = []

alunos.append("Guilherme")
alunos.append("Victor")
alunos.append("Pedro")

print(f"alunos[0] {alunos[0]}")
print(f"alunos[1] {alunos[1]}")
print(f"alunos[1] {alunos[-1]}")

alunos[1] = "Anna"

print(alunos)

alunos.insert(1, "Sophia")

print(alunos)

# sem parâmetros, remove ultimo / com parametro, remove por indice

alunos.remove("Guilherme")

print(alunos)

alunos.pop(1)

print(alunos)

tamanho_lista = len(alunos)

print(f"tamanho lista {tamanho_lista}")