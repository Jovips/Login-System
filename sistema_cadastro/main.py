import sqlite3

def criar_tabela_usuarios():
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (email TEXT, senha TEXT)")
    conexao.commit()
    conexao.close()

def fazer_login():
    email = input("Informe o e-mail: ")
    senha = input("Informe a senha: ")

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha))
    usuario = cursor.fetchone()

    if usuario:
        print("Login bem-sucedido!")
    else:
        print("E-mail ou senha incorretos.")

    conexao.close()

def fazer_cadastro():
    email = input("Cadastre um e-mail válido: ")
    senha = input("Informe uma senha válida: ")

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
    conexao.commit()

    print("Cadastro realizado com sucesso!")

    conexao.close()

def menu():
    print("1 - Fazer Login")
    print("2 - Fazer Cadastro")
    print("3 - Sair")

    escolha = input("Escolha a opção: ")

    if escolha == '1':
        fazer_login()
    elif escolha == '2':
        fazer_cadastro()
    elif escolha == '3':
        print("Saindo do programa.")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    criar_tabela_usuarios()

    while True:
        menu()
        if input("Deseja sair? (s/n): ").lower() == 's':
            break
