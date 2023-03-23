#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Importação da biblioteca

import customtkinter as ctk

# Definindo as cores

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


#Criação da janela

janela = ctk.CTk()
janela.geometry("600x400")
janela.title("Registro de Transações")

# Criação dos campos de entrada
        
cod_banco = ctk.CTkLabel(janela, text="Código Banco:")
cod_banco.grid(row=0, column=0, padx=5, pady=5)

cod_banco = ctk.CTkEntry(janela)
cod_banco.grid(row=0, column=1, padx=5, pady=5)

nome_banco = ctk.CTkLabel(janela, text="Nome Banco")
nome_banco.grid(row=1, column=0, padx=5, pady=5)

nome_banco = ctk.CTkEntry(janela)
nome_banco.grid(row=1, column=1, padx=5, pady=5)

agencia_origem = ctk.CTkLabel(janela, text="Agência de origem:")
agencia_origem.grid(row=2, column=0, padx=5, pady=5)

agencia_origem = ctk.CTkEntry(janela)
agencia_origem.grid(row=2, column=1, padx=5, pady=5)

conta_origem = ctk.CTkLabel(janela, text="Conta de origem:")
conta_origem.grid(row=3, column=0, padx=5, pady=5)

conta_origem = ctk.CTkEntry(janela)
conta_origem.grid(row=3, column=1, padx=5, pady=5)

agencia_destino = ctk.CTkLabel(janela, text="Agência de destino:")
agencia_destino.grid(row=4, column=0, padx=5, pady=5)

agencia_destino = ctk.CTkEntry(janela)
agencia_destino.grid(row=4, column=1, padx=5, pady=5)

conta_destino = ctk.CTkLabel(janela, text="Conta de destino:")
conta_destino.grid(row=5, column=0, padx=5, pady=5)

ent_conta_destino = ctk.CTkEntry(janela)
ent_conta_destino.grid(row=5, column=1, padx=5, pady=5)

valor = ctk.CTkLabel(janela, text="Valor:")
valor.grid(row=6, column=0, padx=5, pady=5)

ent_valor = ctk.CTkEntry(janela)
ent_valor.grid(row=6, column=1, padx=5, pady=5)

# Criação dos botões
        
checkbox_deposito = ctk.CTkCheckBox(janela, text="Depósito")
checkbox_deposito.grid(row=7, column=0, padx=5, pady=5)

checkbox_saques = ctk.CTkCheckBox(janela, text="Saque")
checkbox_saques.grid(row=7, column=1, padx=5, pady=5)

checkbox_transferencia = ctk.CTkCheckBox(janela, text="Transferência")
checkbox_transferencia.grid(row=7, column=2, padx=5, pady=5)

checkbox_estorno = ctk.CTkCheckBox(janela, text="Estorno")
checkbox_estorno.grid(row=7, column=3, padx=5, pady=5)
        
checkbox_pix = ctk.CTkCheckBox(janela, text="Pix")
checkbox_pix.grid(row=7, column=4, padx=5, pady=5)
        
checkbox_confirmar = ctk.CTkButton(janela, text="Confirmar")
checkbox_confirmar.grid(row=8, column=0, padx=5, pady=5)

checkbox_cancelar = ctk.CTkButton(janela, text="Cancelar")
checkbox_cancelar.grid(row=8, column=1, padx=5, pady=5)


janela.mainloop()


# In[ ]:




