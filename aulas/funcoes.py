# def saudacao():
#     print("Olá, mundo")

# saudacao()

# def saudacao_com_nome(nome):
#     print(f"Olá, meu nome é {nome}")

# saudacao_com_nome("Guilherme")
# saudacao_com_nome("Douglas")

# def somar(a, b):
#     soma = a + b
#     return soma

# print(somar(5, 2))

def cadastrar_usuario(nome, idade=18):
    print(f"cadastrando nome {nome} {type(nome)}")
    print(f"cadastrando idade {idade} {type(idade)}")

cadastrar_usuario("Lucas Ariel", 20)
cadastrar_usuario("Vitor")

cadastrar_usuario(nome="Douglas", idade=34)
cadastrar_usuario(idade=52, nome="Jair")