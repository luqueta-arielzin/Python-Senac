#E
soma = 4 + 5
multiplicacao = 2 * 6

if soma > 10 and multiplicacao > 10:
        print("a soma e multiplicação são maiores que 10")
else:
        print("a soma e a multiplicação não são maiores que 10")


#OU
if soma > 11 or multiplicacao > 11:
    print("a soma ou multiplicação são maiores que 11")
else:
    print("nem a soma nem a multiplicação são maiores que 11")


#NEGACAO
if not soma > 10:
        print("A soma não é maior que 10")