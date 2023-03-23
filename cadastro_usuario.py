# Importação biblioteca

import customtkinter as ctk

#Definição das cores

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Criação da janela

janela = ctk.CTk()
janela.geometry("800x600")
janela.title("Cadastro de Usuário")

def clique():
    print('Cadastar')

# Agências Bancárias

agencia_label = ctk.CTkLabel(janela, text=r"Número da Agência:")
agencia_label.grid(row=1, column=0, padx=5, pady=5)

agencia_entry = ctk.CTkEntry(janela, width=200)
agencia_entry.grid(row=1, column=1, padx=5, pady=5)

endereco_label = ctk.CTkLabel(janela, text=r"Endereço:")
endereco_label.grid(row=2, column=0, padx=5, pady=5)

endereco_entry = ctk.CTkEntry(janela, width=200)
endereco_entry.grid(row=2, column=1, padx=5, pady=5)

# Contas Bancárias

conta_label = ctk.CTkLabel(janela, text=r"Número da Conta:")
conta_label.grid(row=3, column=0, padx=5, pady=5)

conta_entry = ctk.CTkEntry(janela, width=200)
conta_entry.grid(row=3, column=1, padx=5, pady=5)

limite_label = ctk.CTkLabel(janela, text=r"Limite:")
limite_label.grid(row=4, column=0, padx=5, pady=5)

limite_entry = ctk.CTkEntry(janela, width=200)
limite_entry.grid(row=4, column=1, padx=5, pady=5)

# Movimentações da Conta

data_label = ctk.CTkLabel(janela, text=r"Data da Movimentação:")
data_label.grid(row=5, column=0, padx=5, pady=5)

data_entry = ctk.CTkEntry(janela, width=200)
data_entry.grid(row=5, column=1, padx=5, pady=5)

valor_label = ctk.CTkLabel(janela, text=r"Valor:")
valor_label.grid(row=6, column=0, padx=5, pady=5)

valor_entry = ctk.CTkEntry(janela, width=200)
valor_entry.grid(row=6, column=1, padx=5, pady=5)

tipo_label = ctk.CTkLabel(janela, text=r"Tipo de Movimentação:")
tipo_label.grid(row=7, column=0, padx=5, pady=5)

checkbox = ctk.CTkCheckBox(janela, text='Saque')
checkbox.grid(row=7, column=1, padx=5, pady=5)

checkbox = ctk.CTkCheckBox(janela, text='Depósito')
checkbox.grid(row=7, column=2, padx=5, pady=5)

# tipo_entry = ctk.CTkEntry(janela, width=200)
# tipo_entry.grid(row=7, column=1, padx=5, pady=5)

# Cadastro Usuário e Senha

usuario_label = ctk.CTkLabel(janela, text=r"Usuário:")
usuario_label.grid(row=8, column=0, padx=5, pady=5)

usuario_entry = ctk.CTkEntry(janela, width=200)
usuario_entry.grid(row=8, column=1, padx=5, pady=5)

senha_label = ctk.CTkLabel(janela, text=r"Cadastre sua senha:")
senha_label.grid(row=9, column=0, padx=5, pady=5)

senha_entry = ctk.CTkEntry(janela, show='*', width=200)
senha_entry.grid(row=9, column=1, padx=5, pady=5)

confirmacao_senha_label = ctk.CTkLabel(janela, text=r"Confirme sua senha:")
confirmacao_senha_label.grid(row=10, column=0, padx=5, pady=5)

confirmacao_senha_entry = ctk.CTkEntry(janela, show='*', width=200)
confirmacao_senha_entry.grid(row=10, column=1, padx=5, pady=5)

botao = ctk.CTkButton(janela, text="Cadastrar")
botao.grid(padx=7, pady=5)

janela.mainloop()

