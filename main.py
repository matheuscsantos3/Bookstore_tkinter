import tkinter as tk
from tkinter import ttk, messagebox
from services.gerenciador import GerenciadorLivros

class LivrariaApp:
    def __init__(self, root):
        self.gerenciador = GerenciadorLivros()
        self.root = root
        self.root.title("Livraria")
        self.root.geometry("620x400")
        self.root.configure(bg="#121212")

        self.estilo_widgets()
        self.titulo = tk.Label(root, text="Livraria", font=("Helvetica", 20, "bold"), bg="#121212", fg="#FFFFFF")
        self.titulo.pack(pady=20)

        self.frame = tk.Frame(root, bg="#121212")
        self.frame.pack(pady=20)

        self.btn_cadastrar = ttk.Button(self.frame, text="Cadastrar Livro", command=self.abrir_cadastro)
        self.btn_cadastrar.grid(row=0, column=0, padx=20)

        self.btn_consultar = ttk.Button(self.frame, text="Consultar Livros", command=self.consultar_livros)
        self.btn_consultar.grid(row=0, column=1, padx=20)

        self.btn_remover = ttk.Button(self.frame, text="Remover Livro", command=self.remover_livro)
        self.btn_remover.grid(row=0, column=2, padx=20)

    def estilo_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Helvetica", 11), padding=10, background="#FFFFFF", foreground="#121212")
        style.map("TButton", background=[("active", "#DDDDDD")], foreground=[("disabled", "#666666")])

    def abrir_cadastro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Cadastrar Livro")
        janela.geometry("300x250")
        janela.configure(bg="#121212")

        campos = ["Nome", "Autor", "Editora"]
        entradas = {}

        for campo in campos:
            tk.Label(janela, text=f"{campo}:", bg="#121212", fg="#FFFFFF", font=("Helvetica", 10)).pack(pady=5)
            entrada = tk.Entry(janela, bg="#FFFFFF", fg="#000000")
            entrada.pack()
            entradas[campo.lower()] = entrada

        def salvar():
            nome = entradas["nome"].get()
            autor = entradas["autor"].get()
            editora = entradas["editora"].get()
            if nome and autor and editora:
                livro = self.gerenciador.adicionar_livro(nome, autor, editora)
                messagebox.showinfo("Sucesso", f"Livro ID {livro.id} cadastrado!")
                janela.destroy()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos.")

        ttk.Button(janela, text="Salvar", command=salvar).pack(pady=15)

    def consultar_livros(self):
        janela = tk.Toplevel(self.root)
        janela.title("Livros Cadastrados")
        janela.geometry("500x300")
        janela.configure(bg="#121212")

        tree = ttk.Treeview(janela, columns=("ID", "Nome", "Autor", "Editora"), show="headings")
        for col in ("ID", "Nome", "Autor", "Editora"):
            tree.heading(col, text=col)
        for livro in self.gerenciador.consultar_todos():
            tree.insert("", "end", values=(livro.id, livro.nome, livro.autor, livro.editora))

        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def remover_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Remover Livro")
        janela.geometry("300x150")
        janela.configure(bg="#121212")

        tk.Label(janela, text="Informe o ID do livro:", bg="#121212", fg="#FFFFFF", font=("Helvetica", 10)).pack(pady=10)
        id_entry = tk.Entry(janela, bg="#FFFFFF", fg="#000000")
        id_entry.pack()

        def remover():
            try:
                id_remover = int(id_entry.get())
                livro = self.gerenciador.consultar_por_id(id_remover)
                if livro:
                    self.gerenciador.remover_livro(id_remover)
                    messagebox.showinfo("Removido", f"Livro ID {id_remover} removido.")
                    janela.destroy()
                else:
                    messagebox.showwarning("Erro", "ID não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "ID inválido.")

        ttk.Button(janela, text="Remover", command=remover).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LivrariaApp(root)
    root.mainloop()
