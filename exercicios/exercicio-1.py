print("MÉDIA ESCOLAR DO ALUNO")

nome = input("Olá aluno, qual é seu nome? ")

try:
    nota1 = float(input("Qual foi a sua primeira nota?"))
    nota2 = float(input("Qual foi a sua segunda nota?"))
    nota3 = float(input("Qual foi a sua terceira nota?"))
            
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
        print("Erro: as notas devem estar entre 0 e 10! ")
    else:
        media = (nota1 + nota2 + nota3) / 3

        print("\n---- RESULTADO ----")
        print(f"Aluno: {nome}")
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Nota 3: {nota3}")
        print(f"Média Final: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

except Exception:
    print("Erro: digite apenas números válidos para as notas.")


