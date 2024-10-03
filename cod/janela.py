'''
from tkinter import *

janela = Tk()
janela.geometry('500x500')

def clique():
    print('Fazer login')


texto = Label(janela, text='fazer login')
texto.pack(padx=10, pady=10)

botao = Button(janela, text='Fazer login', command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()

'''

import customtkinter


janela = customtkinter.CTk()
janela.geometry('500x500')

def clique():
    print('Fazer login')

texto = customtkinter.CTkLabel(janela, text='Fazer login', font=('Inter', 20))
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='seu email')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='sua senha', show='*')
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="fazer login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()