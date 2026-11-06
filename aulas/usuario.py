class Usuario():
    def __init__(self, nome, idade, nome_cachorro):
        self.nome = nome
        self.idade = idade
        self.nome_cachorro = nome_cachorro

    def __str__(self):
        return f"O nome do objeto é {self.nome}"


    def apresentar(self):
        print(f"Olá! meu nome é {self.nome} e tenho {self.idade} anos")

    def apresentacao_cachorro(self):
        print(f"O meu cachorro se chama {self.nome_cachorro}")
