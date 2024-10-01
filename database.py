import sqlite3


def criar_banco_dados():
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()

    # Criação da tabela livros
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        ano_publicacao INTEGER,
                        preco REAL
                      )''')

    conn.commit()
    conn.close()


def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                   (titulo, autor, ano_publicacao, preco))
    conn.commit()
    conn.close()


def exibir_livros():
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return livros


def atualizar_preco(livro_id, novo_preco):
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))
    conn.commit()
    conn.close()


def remover_livro(livro_id):
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()


def buscar_livros_por_autor(autor):
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
    livros = cursor.fetchall()
    conn.close()
    return livros
