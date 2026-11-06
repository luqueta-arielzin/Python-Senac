usuario = {
    "nome": "Lucas Ariel",
    "email": "ariel@email.com",
    "idade": 20,
    "ativo": True

}

print(usuario)
print(f"nome: {usuario["nome"]}")

usuario["idade"] = 20
usuario["cidade"] = "Venâncio Aires"

print(f"nova idade {usuario["idade"]}")
print(f"cidade {usuario["cidade"]}")

del usuario["idade"]
usuario.pop("ativo")

print(usuario)

for chave, valor in usuario.items():
    print(f"chave: {chave} | valor: {valor}")