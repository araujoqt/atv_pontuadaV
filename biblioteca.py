import os 
os.system("clear || cls")


from dataclasses import dataclass

livros = []

@dataclass
class Livro:
    titulo: str
    autor: str
    disponivel: bool = True

##Função para salvar os livros no arquivo
def salvar_livros():
    arq = open("lista.txt", "w")
    for livro in livros:
        if livro.disponivel == True:
            status = "Disponível"
        if livro.disponivel == False:
            status = "Não disponível"
        texto = "Livro: " + livro.titulo + " - Autor: " + livro.autor + " - " + status + "\n"
        arq.write(texto)
    arq.close()

def adicionar_livro(titulo, autor):
    novo = Livro(titulo, autor, True)
    livros.append(novo)
    salvar_livros()
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        print("Lista de livros:")
        for i in range(len(livros)):
            livro = livros[i]
            if livro.disponivel == True:
                status = "Disponível"
            if livro.disponivel == False:
                status = "Não disponível"
            print(str(i + 1) + ". " + livro.titulo + " - " + livro.autor + " (" + status + ")")

def emprestar_livro(titulo):
    for i in range(len(livros)):
        livro = livros[i]
        if livro.titulo.lower() == titulo.lower():
            if livro.disponivel == True:
                livro.disponivel = False
                salvar_livros()
                print("Livro emprestado com sucesso!")
                return
            if livro.disponivel == False:
                print("Este livro já está emprestado.")
                return
    print("Livro não encontrado.")

def devolver_livro(titulo):
    for i in range(len(livros)):
        livro = livros[i]
        if livro.titulo.lower() == titulo.lower():
            if livro.disponivel == False:
                livro.disponivel = True
                salvar_livros()
                print("Livro devolvido com sucesso!")
                return
            if livro.disponivel == True:
                print("Este livro já está disponível.")
                return
    print("Livro não encontrado.")

