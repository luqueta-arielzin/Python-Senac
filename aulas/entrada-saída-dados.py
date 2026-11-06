print("Primeira entrada de dados no python")

nome = input("Qual é seu nome? ")

try:
    idade = int(input("Qual é a sua idade? ")) # int para criar ou transformar em inteiro
    print(F"Olá, {nome}. Você tem {idade} anos.")
    if idade <= 12:
        print("É criança")
    elif idade <= 18:
        print("É adolescente")
    else:
        print("É adulto")
except Exception:
    print("O valor da idade não é válido")

