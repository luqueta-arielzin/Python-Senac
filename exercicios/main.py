from gerenciamento_visitantes import (
    carregar_visitantes,
    cadastrar_visitante,
    remover_visitante,
    listar_visitantes,
    ordenar_visitantes,
    filtrar_visitantes,
    consultar_visitante,
    consultar_por_data,
    estatisticas_visitantes
)



# MENU PRINCIPAL


visitantes = carregar_visitantes()

while True:

    print("\n========================================")
    print("             PARQUE AVENTURA")
    print("========================================")
    print()
    print("1 - Cadastrar visitante")
    print("2 - Remover visitante")
    print("3 - Listar visitantes")
    print("4 - Ordenar visitantes")
    print("5 - Filtrar visitantes")
    print("6 - Consultar visitante")
    print("7 - Consultar por data da visita")
    print("8 - Estatísticas dos visitantes")
    print("0 - Encerrar programa")
    print()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_visitante(visitantes)

    elif opcao == "2":
        remover_visitante(visitantes)

    elif opcao == "3":
        listar_visitantes(visitantes)

    elif opcao == "4":
        ordenar_visitantes(visitantes)

    elif opcao == "5":
        filtrar_visitantes(visitantes)

    elif opcao == "6":
        consultar_visitante(visitantes)

    elif opcao == "7":
        consultar_por_data(visitantes)

    elif opcao == "8":
        estatisticas_visitantes(visitantes)

    elif opcao == "0":
        print("\nPrograma encerrado!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")