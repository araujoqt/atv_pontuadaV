import os 
os.system("clear || cls")
import biblioteca

def mostrar_menu():
    print("\n--- Biblioteca do Senai ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            biblioteca.adicionar_livro(titulo, autor)

        elif escolha == "2":
            biblioteca.listar_livros()

        elif escolha == "3":
            titulo = input("Digite o título do livro para emprestar: ")
            biblioteca.emprestar_livro(titulo)

        elif escolha == "4":
            titulo = input("Digite o título do livro para devolver: ")
            biblioteca.devolver_livro(titulo)

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
