# Importa as funções de autenticação e gerenciamento de medicamentos
from gerenciamento_usuarios import cadastrar_autenticar_usuario
from gerenciamento_medicamentos import cadastrar_medicamento, listar_medicamentos, excluir_medicamento, editar_medicamento, dispensar_medicamento

# Inicia o loop principal do programa
while True:

    # Verifica se o usuário está autenticado
    autenticado = cadastrar_autenticar_usuario()

    # Se o usuário não estiver autenticado, ele é redirecionado para o menu de autenticação
    if not autenticado:
        print("Você não está autenticado.")
        continue

    # Se o usuário estiver autenticado, ele é redirecionado para o menu principal
    print("---------- MENU ----------")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Excluir medicamento")
    print("4 - Editar medicamento")
    print("5 - Dispensar medicamento")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    # Verifica qual opção o usuário escolheu
    if opcao == "1":
        print("Cadastrando medicamento...")
        cadastrar_medicamento()
    elif opcao == "2":
        print("Listando medicamentos...")
        listar_medicamentos()
    elif opcao == "3":
        print("Excluindo medicamento...")
        excluir_medicamento()
    elif opcao == "4":
        print("Editando medicamento...")
        editar_medicamento()
    elif opcao == "5":
        print("Dispensando medicamento...")
        dispensar_medicamento()
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")

# O usuário é perguntado se deseja continuar
continuar = input("Deseja continuar? (S/N) ").upper()

# Se o usuário responder "N", o programa é encerrado
if continuar == "N":
    print("Programa encerrado.")
