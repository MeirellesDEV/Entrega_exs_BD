import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#EXERCÍCIO 01
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(255), idade INT, curso VARCHAR(255));')

#EXERCÍCIO 02
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Liandra", 10, "Engenharia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Aurora", 20, "Biologia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Maria", 30, "Engenharia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Leonardo", 40, "ADS");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Laura", 50, "Psicologia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Pedro", 18, "Literatura");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Lucas", 25, "Engenharia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Rosana", 38, "Geografia");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(9, "Diana", 41, "Direito");')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Yanka", 37, "Engenharia");')

#EXERCÍCIO 03
# dados = cursor.execute('SELECT * FROM alunos;')
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
# dados = cursor.execute('SELECT COUNT(*) AS quantidade FROM alunos;')
# for aluno in dados:
#     print(aluno)

#EXERCÍCIO 04
# cursor.execute('UPDATE alunos SET idade = 21 WHERE nome = "Liandra";')
# cursor.execute('DELETE FROM alunos WHERE id = 7;')

#EXERCÍCIO 05
# cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(255), idade INT, saldo FLOAT);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Jorge", 20, 1000.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Jenifer", 18, 2000.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Claudia", 30, 100.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Gustavo", 40, 150.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Tatiana", 50, 3000.00);')

#EXERCÍCIO 06
# dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30;')
# dados = cursor.execute('SELECT AVG(saldo) AS quantidade FROM clientes;')
# dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1;')
# dados = cursor.execute('SELECT COUNT(*) AS quantidade FROM clientes WHERE saldo > 1000;')
# for cliente in dados:
#     print(cliente)

#EXERCÍCIO 07
# dados = cursor.execute('UPDATE clientes SET saldo = 2500.00 WHERE nome = "Tatiana";')
# dados = cursor.execute('DELETE FROM clientes WHERE id = 4;')

#EXERCÍCIO 08
# cursor.execute('CREATE TABLE compras (id INT,cliente_id INT,produto TEXT,valor REAL);')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "mouse", 100.00);')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 2, "teclado", 200.00);')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 5, "monitor", 300.00);')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 7, "webcam", 400.00);')
# dados = cursor.execute('SELECT c.nome AS nome_cliente, p.produto AS compra, p.valor AS valor_compra FROM clientes c JOIN compras p ON c.id = p.cliente_id')
# for cliente in dados:
#     print(cliente)

conexao.commit()
conexao.close