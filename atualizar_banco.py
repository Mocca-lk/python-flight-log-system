import sqlite3

conn = sqlite3.connect('manutencao_aero.db')
cursor = conn.cursor()

try:
    # O comando mágico para adicionar uma coluna sem apagar a tabela
    cursor.execute('ALTER TABLE logs ADD COLUMN status TEXT DEFAULT "Não Informado"')
    conn.commit()
    print("Coluna 'status' adicionada com sucesso!")
except sqlite3.OperationalError:
    # Se você rodar duas vezes, ele vai dar erro porque a coluna já existe
    print("A coluna 'status' já existe no banco de dados.")

conn.close()