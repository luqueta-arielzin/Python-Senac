
contador = 1
soma = 0

while contador <= 5:
    try:
        numero_input = input(f"Digite o numero {contador} a ser somado ")

        numero = int(numero_input)
        soma += numero
        contador += 1
    except Exception:
        print("Insira um número válido")
print(f"a soma total é {soma}")    
    
