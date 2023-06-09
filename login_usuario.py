#!/usr/bin/env python
# coding: utf-8


# Importação biblioteca

import customtkinter as ctk

# Definindo as cores

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criação da janela

janela = ctk.CTk()
janela.geometry("500x300")
janela.title("Login Usuário")


# Criando os campos E-mail e Senha

texto = ctk.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=10, pady=10)

email = ctk.CTkEntry(janela, placeholder_text= "Seu e-mail")
email.pack(padx=10, pady=10)

senha = ctk.CTkEntry(janela, placeholder_text= "Seu senha", show='*')
senha.pack(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(janela, text='Esquece minha senha')
checkbox.pack(padx=10, pady=10)

botao = ctk.CTkButton(janela, text='Login')
botao.pack(padx=10, pady=10)

# Definindo a função que será executada quando o botão de login for clicado

def fazer_login():
    usuario = email.get()
    senha = senha.get()
    if usuario == "usuario" and senha == "senha":
        print("Login bem sucedido!")
    else:
        print("Usuário ou senha incorretos.")


janela.mainloop()

