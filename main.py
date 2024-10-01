from database import (adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_livros_por_autor,
                      criar_banco_dados)
from backup import fazer_backup, limpar_backups
from csv_operations import exportar_csv, importar_csv
from file_manager import criar_diretorios


def menu():
    criar_diretorios()
    criar_banco_dados()

    while True:
        print("\n1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = int(input("Ano de Publicação: "))
            preco = float(input("Preço: "))
            adicionar_livro(titulo, autor, ano_publicacao, preco)
            fazer_backup()
        elif escolha == "2":
            livros = exibir_livros()
            for livro in livros:
                print(livro)
        elif escolha == "3":
            livro_id = int(input("ID do Livro: "))
            novo_preco = float(input("Novo Preço: "))
            atualizar_preco(livro_id, novo_preco)
            fazer_backup()
        elif escolha == "4":
            livro_id = int(input("ID do Livro: "))
            remover_livro(livro_id)
            fazer_backup()
        elif escolha == "5":
            autor = input("Autor: ")
            livros = buscar_livros_por_autor(autor)
            for livro in livros:
                print(livro)
        elif escolha == "6":
            exportar_csv()
        elif escolha == "7":
            caminho_csv = input("Caminho do arquivo CSV: ")
            importar_csv(caminho_csv)
            fazer_backup()
        elif escolha == "8":
            fazer_backup()
        elif escolha == "9":
            limpar_backups()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
