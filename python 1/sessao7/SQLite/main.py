import sqlite3

conexao = sqlite3.connect('/Users/renatomota/Desktop/Python/python 1/sessao7/SQLite/basededados.db')

cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
# 'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
# 'nome TEXT, '
# 'idade INTEGER, '
# 'peso REAL'
# ')')

# cursor.execute('INSERT INTO clientes (nome, idade, peso) VALUES (?,?,?)', ('luna', 2, 12.5))
# cursor.execute('INSERT INTO clientes (nome, idade, peso) VALUES (?,?,?)', ('habigail', 26, 56))
# cursor.execute('INSERT INTO clientes (nome, idade, peso) VALUES (?,?,?)', ('marjorie', 2, 11.5))
# conexao.commit()

# cursor.execute(
# #   'UPDATE clientes SET nome = ? WHERE id = ?',
# #   ('jonson', 2)
# # )

# cursor.execute(
#   'DELETE FROM clientes WHERE id = ?',
#   ('5')

# )
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
  identificador, nome, idade, peso = linha
  print(identificador, nome, idade, peso)

cursor.close()
conexao.close()