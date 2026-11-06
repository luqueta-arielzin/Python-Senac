from usuario import Usuario

print("Execução normal do arquivo...")
usuario = Usuario("Lucas Ariel", 20, "Bilu")
print(f"objeto usuario: {usuario}")

print(usuario.nome)
print(usuario.idade)

usuario.idade = 21

print(f"Nova idade {usuario.idade}")
usuario.apresentar()
usuario.apresentacao_cachorro()


