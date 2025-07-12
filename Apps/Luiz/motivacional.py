import tkinter as tk
import requests
from deep_translator import GoogleTranslator

def buscar_conselho():
    try:
        resposta = requests.get('https://api.adviceslip.com/advice', timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        conselho_ingles = dados['slip']['advice']

        # Traduz para português
        conselho_pt = GoogleTranslator(source='auto', target='pt').translate(conselho_ingles)

        rotulo.config(text=conselho_pt)
    except Exception as e:
        rotulo.config(text=f"Erro ao buscar conselho: {e}")

janela = tk.Tk()
janela.title("Conselhos Traduzidos da API")
janela.geometry("500x220")
janela.config(bg="#f0f0f0")

tk.Label(janela, text="Clique para receber um conselho:", font=("Arial", 14), bg="#f0f0f0").pack(pady=20)

rotulo = tk.Label(janela, text="", font=("Arial", 12), bg="#f0f0f0", wraplength=450, justify="center")
rotulo.pack(pady=10)

btn = tk.Button(janela, text="Novo Conselho", font=("Arial", 12), command=buscar_conselho)
btn.pack(pady=10)

buscar_conselho()

janela.mainloop()
