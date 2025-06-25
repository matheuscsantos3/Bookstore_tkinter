from models.livro import Livro

class GerenciadorLivros:
    def __init__(self):
        self.livros = []
        self.id_global = 0

    def adicionar_livro(self, nome, autor, editora):
        self.id_global += 1
        livro = Livro(self.id_global, nome, autor, editora)
        self.livros.append(livro)
        return livro

    def consultar_todos(self):
        return self.livros

    def consultar_por_id(self, id):
        return next((livro for livro in self.livros if livro.id == id), None)

    def remover_livro(self, id):
        self.livros = [livro for livro in self.livros if livro.id != id]
