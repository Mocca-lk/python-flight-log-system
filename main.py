import sqlite3

# 1. Conexão ou criação do banco de dados
conexao = sqlite3.connect('manutencao_aero.db')
cursor = conexao.cursor()

# 2. Criação do banco de dados com as colunas 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prefixo TEXT NOT NULL,
        descricao TEXT NOT NULL,
        data TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')
# Parte em que o usuário pode adicionar uma manutenção realizada ou pendente:
def registrar_manutencao():
    prefixo = input("Digite o prefixo da aeronave (Ex: PT-XYZ): ")
    descricao = input("Descrição do serviço realizado: ")
    data = "19/01/2026"
    status = input("Status (ex: Pronto para Voo / Em Manutenção): ")
    
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO logs (prefixo, descricao, data, status) VALUES (?, ?, ?, ?)", (prefixo, descricao, data, status))
    conexao.commit()
    print("\n✅ Manutenção registrada com sucesso!\n")

# Opção em que o usuário pode apenas ver as manutenções já registradas/ histórico
def listar_manutencoes():
    print("\n--- HISTÓRICO DE MANUTENÇÕES ---")
    cursor.execute("SELECT * FROM logs")
    for linha in cursor.fetchall():
        
       print(f"ID: {linha[0]} | Avião: {linha[1]} | Serviço: {linha[2]} | Data: {linha[3]} | Status: {linha[4]}")
    print("---------------------------------\n")


# 3. Menu Principal com as opções existentes
while True:
    print("1. Registrar Manutenção")
    print("2. Listar Histórico")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        registrar_manutencao()
    elif opcao == '2':
        listar_manutencoes()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")

conexao.close()