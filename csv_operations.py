import csv
import sqlite3


def exportar_csv():
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()

    # Escrevendo dados no arquivo CSV
    with open("meu_sistema_livraria/exports/livros_exportados.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "titulo", "autor", "ano_publicacao", "preco"])
        writer.writerows(livros)

    print("Dados exportados com sucesso!")


def importar_csv(caminho_csv):
    conn = sqlite3.connect("meu_sistema_livraria/data/livraria.db")
    cursor = conn.cursor()

    with open(caminho_csv, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                           (row["titulo"], row["autor"], row["ano_publicacao"], row["preco"]))

    conn.commit()
    conn.close()

    print("Dados importados com sucesso!")
