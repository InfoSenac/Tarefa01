import tkinter.messagebox
from customtkinter import *
import tkinter
import requests

set_appearance_mode('dark')
set_default_color_theme('green')

janela = CTk()
janela.title('Busca Endereço')
janela.geometry('500x270')
janela.resizable(False, False)

def consultar_api(cep):
    return requests.get(url=f'https://viacep.com.br/ws/{cep}/json/').json()

def buscar_cep():
    cep = en_cep.get()
    if len(cep) == 8 and cep.isnumeric():
        endereco = consultar_api(cep=cep)
        if not 'erro' in endereco:
            lb_logradouro.configure(text=endereco['logradouro'])
            lb_complemento.configure(text=endereco['complemento'])
            lb_bairro.configure(text=endereco['bairro'])
            lb_localidade.configure(text=endereco['localidade'])
            lb_uf.configure(text=endereco['uf'])
        else:
            tkinter.messagebox.showinfo('Informação', 'CEP não encontrado.')
    else:
            tkinter.messagebox.showerror('Erro','CEP Inválido!')
            
def copiar_dados():
    texto = lb_logradouro.cget('text')
    janela.clipboard_clear()
    janela.clipboard_append(texto)
    tkinter.messagebox.showinfo('Copiar', 'Dados copiados! ')


def excluir_dados():
    lb_logradouro.configure(text='')
    lb_localidade.configure(text='')
    lb_bairro.configure(text='')
    lb_complemento.configure(text='')
    lb_uf.configure(text='')
    en_cep.delete('0',END)


CTkLabel(janela, text='Busca Endereço', font=('Verdana', 22, 'bold')).place(x=150, y=20)
CTkLabel(janela, text='logradouro:', font=('Arial', 15, 'bold')).place(x=20, y=135)
CTkLabel(janela, text='Complemento:', font=('Arial', 15, 'bold')).place(x=340, y=135)
CTkLabel(janela, text='Bairro:', font=('Arial', 15, 'bold')).place(x=20, y=195)
CTkLabel(janela, text='Cidade:', font=('Arial', 15, 'bold')).place(x=190, y=195)
CTkLabel(janela, text='UF:', font=('Arial', 15, 'bold')).place(x=410, y=195)

CTkLabel(janela, text='Logradouro:', font=('Arial', 15, 'bold')).place(x=20, y=135)


btn_consulta = CTkButton(janela, text='Buscar', command=buscar_cep)
btn_copiar = CTkButton(janela, text='Copiar', width=60, fg_color='blue', hover_color='blue4', command=copiar_dados)
btn_excluir = CTkButton(janela, text='Excluir', width=60, fg_color='red', hover_color='red4', command=excluir_dados)


en_cep = CTkEntry(janela, width=150, placeholder_text='Digite só 8 números', text_color='black', fg_color='white')
lb_logradouro = CTkLabel(janela, width=300, corner_radius=5, text='', text_color='black', font=('Calibri', 15, 'bold'), fg_color='white')
lb_complemento = CTkLabel(janela, width=140, corner_radius=5, text='', text_color='black', font=('Calibri', 15, 'bold'), fg_color='white')
lb_bairro = CTkLabel(janela, width=170, text='', corner_radius=5, text_color='black', font=('Calibri', 15, 'bold'), fg_color='white')
lb_localidade = CTkLabel(janela, width=200, corner_radius=5, text='', text_color='black', font=('Calibri', 15, 'bold'), fg_color='white')
lb_uf = CTkLabel(janela, text='', width=50, corner_radius=5, text_color='black', font=('Calibri', 15, 'bold'), fg_color='white')

btn_consulta.place(x=180, y=100)
btn_copiar.place(x=340, y=100)
btn_excluir.place(x=420, y=100)
en_cep.place(x=20, y=100)
lb_logradouro.place(x=20, y=160)
lb_complemento.place(x=340, y=160)
lb_bairro.place(x=20, y=220)
lb_localidade.place(x=210, y=220)
lb_uf.place(x=430, y=220)

janela.mainloop()

