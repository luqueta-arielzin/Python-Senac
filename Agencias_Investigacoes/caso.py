from datetime import datetime
import uuid


class Suspeito:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.evidencias = []

    def adicionar_evidencia(self, evidencia):
        self.evidencias.append(evidencia)

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "evidencias": self.evidencias
        }

    @classmethod
    def de_dicionario(cls, dados):
        suspeito = cls(dados["nome"], dados["idade"])
        suspeito.evidencias = dados.get("evidencias", [])
        return suspeito


class Caso:
    def __init__(self, titulo, local):
        self.id = str(uuid.uuid4())[:8]
        self.titulo = titulo
        self.local = local
        self.suspeitos = []
        self.resolvido = False
        self.data_criacao = datetime.now().strftime("%d/%m/%Y")
        self.data_resolucao = None

    def adicionar_suspeito(self, suspeito):
        self.suspeitos.append(suspeito)

    def para_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "local": self.local,
            "suspeitos": [
                suspeito.para_dicionario()
                for suspeito in self.suspeitos
            ],
            "resolvido": self.resolvido,
            "data_criacao": self.data_criacao,
            "data_resolucao": self.data_resolucao
        }

    @classmethod
    def de_dicionario(cls, dados):
        caso = cls(dados["titulo"], dados["local"])

        caso.id = dados["id"]
        caso.resolvido = dados.get("resolvido", False)
        caso.data_criacao = dados.get("data_criacao")
        caso.data_resolucao = dados.get("data_resolucao")

        caso.suspeitos = [
            Suspeito.de_dicionario(suspeito)
            for suspeito in dados.get("suspeitos", [])
        ]

        return caso