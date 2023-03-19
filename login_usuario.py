#!/usr/bin/env python
# coding: utf-8

# In[26]:


import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print('Fazer Login')

texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text= "Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text= "Seu senha", show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Esquece minha senha')
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Login')
botao.pack(padx=10, pady=10)


janela.mainloop()

