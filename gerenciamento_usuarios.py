import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('usuarios.db')

# Função para cadastrar e autenticar usuários
def cadastrar_autenticar_usuario():
    """
    Esta função cadastra e autentica usuários.

    Args:
        None

    Returns:
        True se o usuário foi autenticado com sucesso, False se não.
    """

    # Pega a opção do usuário
    opcao = input("O que você deseja fazer?\nDigite '1' para cadastrar um novo usuário\nDigite '2' para autenticar um usuário existente\nSua opção: ")

    # Verifica a opção do usuário
    if opcao == '1':
        # Cadastra o novo usuário
        nome = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")

        # Insere o usuário no banco de dados
        conn.execute("INSERT INTO usuarios (NOME, SENHA) VALUES (?, ?)", (nome, senha))

        # Salva as alterações no banco de dados
        conn.commit()

        # Imprime uma mensagem de sucesso
        print("Usuário cadastrado com sucesso!")

        return True
    elif opcao == '2':
        # Autentica o usuário existente
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        # Consulta o banco de dados para verificar se o usuário existe
        cursor = conn.execute("SELECT * FROM usuarios WHERE NOME = ? AND SENHA = ?", (nome, senha))

        # Obtém o resultado da consulta
        resultado = cursor.fetchone()

        # Se o usuário não existir, imprime uma mensagem de erro
        if resultado is None:
            print("Usuário ou senha incorretos.")
            return False

        # Se o usuário existir, imprime uma mensagem de sucesso
        else:
            print("Usuário autenticado com sucesso!")
            return True
    else:
        # Se a opção do usuário for inválida, imprime uma mensagem de erro
        print("Opção inválida.")
        return False
