
import json
from datetime import datetime
from visitante import Visitante


ARQUIVO = "visitantes.json"



# PRA CARREGAR E SALAVAR


def carregar_visitantes():
    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")
        dados = json.load(arquivo)
        arquivo.close()

        visitantes = []

        for dado in dados:
            visitante = Visitante.de_dicionario(dado)
            visitantes.append(visitante)

        return visitantes

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_visitantes(visitantes):
    dados = []

    for visitante in visitantes:
        dados.append(visitante.para_dicionario())

    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()



# VALIDAR DATA DO VISITANTE


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def data_nao_anterior(data):
    data_digitada = datetime.strptime(
        data, "%d/%m/%Y"
    ).date()

    hoje = datetime.now().date()

    return data_digitada >= hoje


# CADASTRAR VISITANTE


def cadastrar_visitante(visitantes):
    print("\n===== CADASTRAR VISITANTE =====")

    nome = input("Nome: ").strip()

    while nome == "":
        print("O nome não pode ficar vazio.")
        nome = input("Nome: ").strip()

    data_nascimento = input(
        "Data de nascimento (DD/MM/AAAA): "
    ).strip()

    while not validar_data(data_nascimento):
        print("Data de nascimento inválida.")
        data_nascimento = input(
            "Data de nascimento (DD/MM/AAAA): "
        ).strip()

    cpf = input("CPF: ").strip()

    while cpf == "":
        print("O CPF não pode ficar vazio.")
        cpf = input("CPF: ").strip()

    cpf_existe = False

    for visitante in visitantes:
        if visitante.cpf == cpf:
            cpf_existe = True

    if cpf_existe:
        print("Já existe um visitante cadastrado com este CPF.")
        print("O cadastro não foi realizado.")
        return

    print("\n1 - Normal")
    print("2 - VIP")
    print("3 - Premium")

    tipo = input("Tipo de ingresso: ").strip()

    while tipo not in ["1", "2", "3"]:
        print("Opção inválida.")
        tipo = input("Tipo de ingresso: ").strip()

    if tipo == "1":
        tipo_ingresso = "Normal"
    elif tipo == "2":
        tipo_ingresso = "VIP"
    else:
        tipo_ingresso = "Premium"

    data_visita = input(
        "Data da visita (DD/MM/AAAA): "
    ).strip()

    while (
        not validar_data(data_visita)
        or not data_nao_anterior(data_visita)
    ):
        print("Data da visita inválida.")
        print(
            "Informe uma data igual ou posterior "
            "à data atual."
        )

        data_visita = input(
            "Data da visita (DD/MM/AAAA): "
        ).strip()

    visitante = Visitante(
        nome,
        data_nascimento,
        cpf,
        tipo_ingresso,
        data_visita
    )

    visitantes.append(visitante)
    salvar_visitantes(visitantes)

    print("\nVisitante cadastrado com sucesso!")
    print("Número do ingresso:", visitante.numero_ingresso)


# REMOVER VISITANTE


def remover_visitante(visitantes):
    cpf = input("Digite o CPF do visitante: ").strip()

    for visitante in visitantes:
        if visitante.cpf == cpf:
            visitantes.remove(visitante)
            salvar_visitantes(visitantes)

            print("Visitante removido com sucesso!")
            return

    print("Nenhum visitante encontrado com esse CPF.")



# LISTAR VISITANTES


def listar_visitantes(visitantes):
    print("\n===== VISITANTES =====")

    if len(visitantes) == 0:
        print("Nenhum visitante cadastrado.")
        return

    for visitante in visitantes:
        print("\nNome:", visitante.nome)
        print("Idade:", visitante.calcular_idade())
        print("Ingresso:", visitante.tipo_ingresso)


# ORDENAR VISITANTES


def ordenar_visitantes(visitantes):
    print("\n1 - Ordenar por nome")
    print("2 - Ordenar por idade")

    escolha = input("Escolha: ").strip()

    if escolha == "1":
        visitantes.sort(
            key=lambda visitante: visitante.nome.lower()
        )

    elif escolha == "2":
        visitantes.sort(
            key=lambda visitante: visitante.calcular_idade()
        )

    else:
        print("Opção inválida.")
        return

    salvar_visitantes(visitantes)

    print("\nVisitantes ordenados:")
    listar_visitantes(visitantes)



# FILTRAR POR TIPO DE INGRESSO


def filtrar_visitantes(visitantes):
    print("\n1 - Normal")
    print("2 - VIP")
    print("3 - Premium")

    escolha = input("Escolha: ").strip()

    if escolha == "1":
        tipo = "Normal"
    elif escolha == "2":
        tipo = "VIP"
    elif escolha == "3":
        tipo = "Premium"
    else:
        print("Opção inválida.")
        return

    encontrou = False

    print("\nVISITANTES", tipo.upper())

    for visitante in visitantes:
        if visitante.tipo_ingresso == tipo:
            print(
                visitante.nome,
                "-",
                visitante.calcular_idade(),
                "anos"
            )
            encontrou = True

    if not encontrou:
        print("Nenhum visitante encontrado.")


# CONSULTAR PELO CPF

def consultar_visitante(visitantes):
    cpf = input("Digite o CPF: ").strip()

    for visitante in visitantes:
        if visitante.cpf == cpf:
            print("\n===== INGRESSO ENCONTRADO =====")
            print("Nome:", visitante.nome)
            print("Idade:", visitante.calcular_idade(), "anos")
            print("CPF:", visitante.cpf)
            print("Data de nascimento:", visitante.data_nascimento)
            print("Ingresso:", visitante.tipo_ingresso)
            print("Data da visita:", visitante.data_visita)
            print("Número do ingresso:", visitante.numero_ingresso)
            return

    print("Visitante não encontrado.")



# CONSULTAR POR DATA DA VISITA


def consultar_por_data(visitantes):
    data = input(
        "Data da visita (DD/MM/AAAA): "
    ).strip()

    if not validar_data(data):
        print("Data inválida.")
        return

    encontrou = False

    print("\n===== VISITANTES DO DIA", data, "=====")

    for visitante in visitantes:
        if visitante.data_visita == data:
            print(
                visitante.nome,
                "-",
                visitante.calcular_idade(),
                "anos -",
                visitante.tipo_ingresso
            )
            encontrou = True

    if not encontrou:
        print("Nenhum visitante encontrado para esta data.")


# ESTATÍSTICAS


def estatisticas_visitantes(visitantes):
    print("\n===== ESTATÍSTICAS DO PARQUE =====")

    if len(visitantes) == 0:
        print(
            "Não existem visitantes cadastrados "
            "para gerar estatísticas."
        )
        return

    total = len(visitantes)
    normal = 0
    vip = 0
    premium = 0
    soma_idades = 0

    for visitante in visitantes:
        if visitante.tipo_ingresso == "Normal":
            normal += 1
        elif visitante.tipo_ingresso == "VIP":
            vip += 1
        elif visitante.tipo_ingresso == "Premium":
            premium += 1

        soma_idades += visitante.calcular_idade()

    media = soma_idades / total

    print("Total de visitantes:", total)
    print("Ingressos Normal:", normal)
    print("Ingressos VIP:", vip)
    print("Ingressos Premium:", premium)
    print("Média de idade:", round(media, 1), "anos")