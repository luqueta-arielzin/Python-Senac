import uuid


class Visitante:

    def __init__(
        self,
        nome,
        data_nascimento,
        cpf,
        tipo_ingresso,
        data_visita
    ):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.tipo_ingresso = tipo_ingresso
        self.data_visita = data_visita
        self.numero_ingresso = str(uuid.uuid4())

    def calcular_idade(self):
        from datetime import datetime

        nascimento = datetime.strptime(
            self.data_nascimento, "%d/%m/%Y"
        ).date()

        hoje = datetime.now().date()

        idade = hoje.year - nascimento.year

        if (hoje.month, hoje.day) < (
            nascimento.month, nascimento.day
        ):
            idade -= 1

        return idade

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "tipo_ingresso": self.tipo_ingresso,
            "data_visita": self.data_visita,
            "numero_ingresso": self.numero_ingresso
        }

    @classmethod
    def de_dicionario(cls, dados):
        visitante = cls(
            dados["nome"],
            dados["data_nascimento"],
            dados["cpf"],
            dados["tipo_ingresso"],
            dados["data_visita"]
        )

        # PRESERVAR O NUMERO ORIGINAL DO INGRESSO!
        visitante.numero_ingresso = dados["numero_ingresso"]

        return visitante