import tkinter as tk
import requests

def buscar_capital():
    pais = entrada_pais.get()
    if not pais:
        resultado_label.config(text="Digite um país.")
        return

    url = f"https://restcountries.com/v3.1/name/{pais}"
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        capital = dados[0].get("capital", ["Desconhecida"])[0]
        resultado_label.config(text=f"Capital: {capital}")
    except:
        resultado_label.config(text="País não encontrado.")

janela = tk.Tk()
janela.title("Buscar Capital")
janela.geometry("300x150")

tk.Label(janela, text="Nome do país:").pack(pady=5)
entrada_pais = tk.Entry(janela)
entrada_pais.pack()

botao_buscar = tk.Button(janela, text="Buscar", command=buscar_capital)
botao_buscar.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()
