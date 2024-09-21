import tkinter as tk
from tkinter import messagebox

def salvar_treino():
    nome_aluno = entrada_aluno.get()
    nome_treino = treino_selecionado.get()
    repeticoes = entrada_repeticoes.get()
    series = entrada_series.get()

    if nome_aluno and nome_treino and repeticoes and series:
        try:
            repeticoes = int(repeticoes)
            series = int(series)
            # Simular salvamento (pode ser adaptado para salvar em arquivo ou banco de dados)
            messagebox.showinfo("Sucesso", f"Treino de {nome_aluno}: {nome_treino} cadastrado com {repeticoes} repetições e {series} séries!")
            limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Repetições e Séries devem ser números inteiros.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

def limpar_campos():
    entrada_aluno.delete(0, tk.END)
    entrada_repeticoes.delete(0, tk.END)
    entrada_series.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Treinos")

label_aluno = tk.Label(janela, text="Nome do Aluno:")
label_aluno.grid(row=0, column=0, padx=10, pady=10)

entrada_aluno = tk.Entry(janela)
entrada_aluno.grid(row=0, column=1, padx=10, pady=10)

opcoes_treinos = ["Supino", "Agachamento", "Rosca Direta", "Leg Press", "Remada"]

label_treino = tk.Label(janela, text="Selecione o Treino:")
label_treino.grid(row=1, column=0, padx=10, pady=10)

treino_selecionado = tk.StringVar(janela)
treino_selecionado.set(opcoes_treinos[0])

menu_treino = tk.OptionMenu(janela, treino_selecionado, *opcoes_treinos)
menu_treino.grid(row=1, column=1, padx=10, pady=10)

label_repeticoes = tk.Label(janela, text="Número de Repetições:")
label_repeticoes.grid(row=2, column=0, padx=10, pady=10)

entrada_repeticoes = tk.Entry(janela)
entrada_repeticoes.grid(row=2, column=1, padx=10, pady=10)

label_series = tk.Label(janela, text="Número de Séries:")
label_series.grid(row=3, column=0, padx=10, pady=10)

entrada_series = tk.Entry(janela)
entrada_series.grid(row=3, column=1, padx=10, pady=10)

botao_salvar = tk.Button(janela, text="Salvar Treino", command=salvar_treino)
botao_salvar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
