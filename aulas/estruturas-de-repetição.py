#contador = 1
#continue = pula a atual e segue
#break = pula todas e sai do while
# while contador <=5:
#     if contador == 3:
#         contador += 1
#         continue
    
#     if contador == 7:
#         break
    
#     print(f"Contador {contador}")
#     contador += 1


# print("usando somente numero final")
# for numero in range(7):
#     print(f"número {numero}")

# print("usando numero inicial e numero final")
# for numero in range(1, 7):
#     print(f"número {numero}")

# print("usando numero inicial, final e incrementel")
# sequencia = range(0, 17, 2)
# for numero in sequencia:
#     print(f"número {numero}")

# print("usando numero inicial, final e incrementel - contador negativo")
# sequencia = range(10, -1, -1)
# for numero in sequencia:
#     print(f"número {numero}")



for letra in "Lucas Ariel":
    print(f"letra {letra}")

frutas = ["Maçã", "Manga", "Melão"]

for fruta in frutas:
    print(f"fruta {fruta}")

print("usando o enumerate")
for indice, fruta in enumerate(frutas):
    print(f"indice {indice} : {fruta}")


print("usando o enumerate e start")
for indice, fruta in enumerate(frutas, start=1):
    print(f"indice {indice} : {fruta}")