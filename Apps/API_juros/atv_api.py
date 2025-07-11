from customtkinter import *
import requests
import toml


set_appearance_mode('dark')

janela = CTk()
janela.geometry('300x300')
janela.resizable(False, False)

def pesquisar(pais):
    token = toml.load("Python\\Tkinter\\atv_api_juros\\secrets.toml")
    
    api_url = f'https://api.api-ninjas.com/v1/interestrate?country={pais}'
    response = requests.get(api_url, headers={'X-Api-Key': token['Api']['Api-Key']})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return print("Error:", response.status_code, response.text)
    
    
#     {
#   "central_bank_rates": [
#     {
#       "central_bank": "Mexican Central Bank",
#       "country": "Mexico",
#       "rate_pct": 8,
#       "last_updated": "06-26-2025"
#     }
#   ]
#   }
    

def gerar_pesquisa():  
    pais = get_pais.get()
    endereco = pesquisar(pais=pais)
    if endereco:
        resultado = f"{endereco['central_bank_rates'][0]['central_bank']},\n{endereco['central_bank_rates'][0]['country']},\n{endereco['central_bank_rates'][0]['rate_pct']}%,\n{endereco['central_bank_rates'][0]['last_updated']}"
        # resultado = endereco.get("central_bank_rates")0]['rate_pct']}% - Última atualização: {endereco.get('last_update', '')
        # resultado = resultado[0]
        # resultado = resultado.get('central_bank')
    else:
        resultado = "Erro ao obter dados. Verifique o nome do país ou a chave da API."
    res.configure(text=resultado)

CTkLabel(janela, text='Verifique Juros: ', font=('Arial', 20, 'bold'), text_color='#fff', width=250).place(x=25, y=15)

get_pais = CTkEntry(janela,placeholder_text='Digite um pais [EN]', width=250, height=30, fg_color='white', text_color='black')
get_pais.place(x=25, y=50)

btn = CTkButton(janela, text='Consultar', width=150, command=gerar_pesquisa)
btn.place(x=77, y=100)

res = CTkLabel(janela, text='RESULTADO', width=250, height=90, fg_color='white', text_color='black', wraplength=250, justify='left')
res.place(x=25, y=135)

janela.mainloop()
