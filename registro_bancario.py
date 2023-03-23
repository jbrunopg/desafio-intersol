import customtkinter as ctk

class Janela(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Registro de Transações")

        # Widgets
        self.lbl_descricao = ctk.CTkLabel(self, text="Descrição:")
        self.lbl_descricao.grid(row=0, column=0)
        self.ent_descricao = ctk.CTkEntry(self)
        self.ent_descricao.grid(row=0, column=1)

        self.lbl_valor = ctk.CTkLabel(self, text="Valor:")
        self.lbl_valor.grid(row=1, column=0)
        self.ent_valor = ctk.CTkEntry(self)
        self.ent_valor.grid(row=1, column=1)


class Janela2(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Registro de Transações")

        # Widgets
        self.lbl_descricao = ctk.CTkLabel(self, text="Descrição:")
        self.lbl_descricao.grid(row=0, column=0)
        self.ent_descricao = ctk.CTkEntry(self)
        self.ent_descricao.grid(row=0, column=1)

        self.lbl_valor = ctk.CTkLabel(self, text="Valor:")
        self.lbl_valor.grid(row=1, column=0)
        self.ent_valor = ctk.CTkEntry(self)
        self.ent_valor.grid(row=1, column=1)

        self.btn_deposito = ctk.CTkButton(self, text="Depósito")
        self.btn_deposito.grid(row=2, column=0)

        self.btn_saque = ctk.CTkButton(self, text="Saque")
        self.btn_saque.grid(row=2, column=1)

        self.btn_estorno = ctk.CTkButton(self, text="Estorno")
        self.btn_estorno.grid(row=2, column=2)

        self.btn_transferencia = ctk.CTkButton(self, text="Transferência")
        self.btn_transferencia.grid(row=2, column=3)


class Janela3(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Registro de Transações")

        # Widgets
        self.lbl_descricao =ctk.CTkLabel(self, text="Descrição:")
        self.lbl_descricao.grid(row=0, column=0)

        self.ent_descricao = ctk.CTkEntry(self)
        self.ent_descricao.grid(row=0, column=1)

        self.lbl_valor = ctk.CTkLabel(self, text="Valor:")
        self.lbl_valor.grid(row=1, column=0)

        self.ent_valor = ctk.CTkEntry(self)
        self.ent_valor.grid(row=1, column=1)

        self.btn_deposito = ctk.CTkButton(self, text="Depósito", command=self.depos)
        self.btn_deposito.grid(row=2, column=0)

        self.btn_saque = ctk.CTkButton(self, text="Saque", command=self.saq)
        self.btn_saque.grid(row=2, column=1)
