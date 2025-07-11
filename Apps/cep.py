import tkinter as tk
from tkinter import messagebox
import requests

def consultar_cep():
    cep = entrada_cep.get().strip().replace("-", "")
    
    if not cep.isdigit() or len(cep) != 8:
        messagebox.showerror("Erro", "Digite um CEP válido com 8 dígitos.")
        return

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
            return

        resultado_texto = (
            f"CEP: {dados['cep']}\n"
            f"Logradouro: {dados['logradouro']}\n"
            f"Bairro: {dados['bairro']}\n"
            f"Cidade: {dados['localidade']}\n"
            f"Estado: {dados['uf']}"
        )
        resultado_label.config(text=resultado_texto)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro na requisição: {e}")

def verificar_cpf():
    cpf = entrada_cpf.get().strip().replace(".", "").replace("-", "")
    
    if not cpf.isdigit() or len(cpf) != 11:
        messagebox.showerror("Erro", "Para confirmar: digite novamente:")
    else:
        messagebox.showinfo("CPF", "CPF cadastrado.")

janela = tk.Tk()
janela.title("Consulta de CEP e CPF")
janela.geometry("400x350")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Consulta de Endereço por CEP", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

frame_entrada_cep = tk.Frame(janela)
frame_entrada_cep.pack(pady=5)

tk.Label(frame_entrada_cep, text="Digite o CEP:").pack(side="left", padx=5)
entrada_cep = tk.Entry(frame_entrada_cep, width=20)
entrada_cep.pack(side="left")

botao_consultar = tk.Button(janela, text="Consultar CEP", command=consultar_cep)
botao_consultar.pack(pady=10)

frame_entrada_cpf = tk.Frame(janela)
frame_entrada_cpf.pack(pady=5)

tk.Label(frame_entrada_cpf, text="Digite o CPF:").pack(side="left", padx=5)
entrada_cpf = tk.Entry(frame_entrada_cpf, width=20)
entrada_cpf.pack(side="left")

botao_cpf = tk.Button(janela, text="Verificar CPF", command=verificar_cpf)
botao_cpf.pack(pady=10)

resultado_label = tk.Label(janela, text="", justify="left", font=("Arial", 12))
resultado_label.pack(pady=10)

janela.mainloop()
