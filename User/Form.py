# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:56:15 2022

@author: Danilo Cabral
"""
# Definição da classe "Form".
class Form:
    # Definição do método construtor.
    def __init__(self, window):
        # O atributo "window" recebe o valor de "window".
        self.window = window
    # Definição do método "predict_with_built_in_gas_cost_predictor()".
    def predict_with_built_in_gas_cost_predictor(self):
        # Importação do módulo "tkinter".
        from tkinter import Label, Entry, Text, Button, StringVar
        # O atributo "from_address_label" recebeo uma instância da classe "Label".
        self.from_address_label = Label(self.window, text = 'From Address')
        # O atributo "to_address_label" recebeo uma instância da classe "Label".
        self.to_address_label = Label(self.window, text = 'To Address')
        # O atributo "gas_limit_label" recebeo uma instância da classe "Label".
        self.gas_limit_label = Label(self.window, text = 'Gas Limit')
        # O atributo "value_label" recebeo uma instância da classe "Label".
        self.value_label = Label(self.window, text = 'Value')
        # O atributo "data_label" recebeo uma instância da classe "Label".
        self.data_label = Label(self.window, text = 'Data')
        # O atributo "data_label" recebeo uma instância da classe "Label".
        self.block_label = Label(self.window, text = 'Current Block')
        # O atributo "block_delta_label" recebeo uma instância da classe "Label".
        self.block_delta_label = Label(self.window, text = 'Block Delta')
        # O atributo "result_label" recebeo uma instância da classe "Label".
        self.result_label = Label(self.window, text = 'Estimated Gas')
        # O atributo "from_address" recebeo uma instância da classe "Entry".
        self.from_address = Entry(width = 110, border = 3)
        # O atributo "to_address" recebeo uma instância da classe "Entry".
        self.to_address = Entry(width = 110, border = 3)
        # O atributo "gas_limit" recebeo uma instância da classe "Entry".
        self.gas_limit = Entry(width = 43, border = 3)
        # O atributo "value" recebeo uma instância da classe "Entry".
        self.value = Entry(width = 43, border = 3)
        # O atributo "data" recebeo uma instância da classe "Text".
        self.data = Text(self.window, width = 82, height = 15, border = 3)
        # O atributo "block" recebeo uma instância da classe "Entry".
        self.block = Entry(width = 43, border = 3)
        # O atributo "block_delta" recebeo uma instância da classe "Entry".
        self.block_delta = Entry(width = 43, border = 3)
        # O atributo "result_text" recebe uma instância de "tk".
        self.result_text = StringVar()
        # O atributo "result" recebeo uma instância da classe "Entry".
        self.result = Entry(width = 43, border = 3, state = 'readonly', textvariable = self.result_text)
        # O atributo "submit" recebeo uma instância da classe "Button".
        self.submit = Button(self.window, text = 'Predict', width = 20, background = 'black', foreground = 'white', border = 3, command = self.get_predict_with_built_in_gas_cost_predictor)
        # Chamada do método "place", do objeto "from_address_label".
        self.from_address_label.place(x = 100, y = 50)
        # Chamada do método "place", do objeto "from_address".
        self.from_address.place(x = 200, y = 50)
        # Chamada do método "place", do objeto "to_address_label".
        self.to_address_label.place(x = 100, y = 100)
        # Chamada do método "place", do objeto "to_address".
        self.to_address.place(x = 200, y = 100)
        # Chamada do método "place", do objeto "gas_limit_label".
        self.gas_limit_label.place(x = 100, y = 150)
        # Chamada do método "place", do objeto "gas_limit".
        self.gas_limit.place(x = 200, y = 150)
        # Chamada do método "place", do objeto "value_label".
        self.value_label.place(x = 500, y = 150)
        # Chamada do método "place", do objeto "value".
        self.value.place(x = 600, y = 150)
        # Chamada do método "place", do objeto "block_label".
        self.block_label.place(x = 100, y = 200)
        # Chamada do método "place", do objeto "block".
        self.block.place(x = 200, y = 200)
        # Chamada do método "place", do objeto "block_delta_label".
        self.block_delta_label.place(x = 500, y = 200)
        # Chamada do método "place", do objeto "block_delta".
        self.block_delta.place(x = 600, y = 200)
        # Chamada do método "place", do objeto "data_label".
        self.data_label.place(x = 100, y = 250)
        # Chamada do método "place", do objeto "data".
        self.data.place(x = 200, y = 250)
        # Chamada do método "place", do objeto "result_label".
        self.result_label.place(x = 100, y = 510)
        # Chamada do método "place", do objeto "result".
        self.result.place(x = 200, y = 510)
        # Chamada do método "place", do objeto "submit".
        self.submit.place(x = 710, y = 510)
    # Definição do método "get_predict_with_built_in_gas_cost_predictor()".
    def get_predict_with_built_in_gas_cost_predictor(self):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../App')
        # Importação do módulo "Application".
        import Application
        # A variável "application" recebe uma instância da classe "Application".
        application = Application.Application()
        # Chamada do método "predict_with_built_in_gas_cost_predictor()", da classe "application".
        self.result_text.set(application.predict_with_built_in_gas_cost_predictor(self.from_address.get(), self.to_address.get(), self.gas_limit.get(), self.value.get(), self.data.get("1.0",'end-1c'), self.block.get()))