# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:23:48 2022

@author: Danilo Cabral.
"""
# Definição da classe "Window".
class Window:
    # Definição do método construtor.
    def __init__(self, mode):
        # Inicialização do atributo "mode".
        self.mode = mode
        # Caso o valor de "self.mode" seja igual a "Built-in Gas Cost Predictor", o script executará o escopo abaixo.
        if (self.mode == 'Built-in Gas Cost Predictor'):
            # Chamada do método "predict_transaction()".
            self.predict_with_built_in_gas_cost_predictor()
    # Definição do método "predict_with_built_in_gas_cost_predictor()".
    def predict_with_built_in_gas_cost_predictor(self):
        # Importação do módulo "tkinter".
        from tkinter import Tk
        # Importação do módulo "Form".
        import Form
        # A variável "window" recebe uma instância da classe "Tk".
        self.window = Tk()
        # A variável "form" recebe uma instância da classe "Form".
        self.form = Form.Form(self.window)
        # Chamada do método "predict_with_built_in_gas_cost_predictor()", do objeto "form".
        self.form.predict_with_built_in_gas_cost_predictor()
        # Chamada do método "title()", do objeto "window".
        self.window.title('Built-in Gas Cost Predictor')
        # Chamada do método "geometry()", do objeto "window".
        self.window.geometry('1000x600+10+10')
        # Chamada do método "iconbitmap()", do objeto "window".
        self.window.iconbitmap('../images/ethereum.ico')
        # Chamada do método "resizable()", do objeto "window".
        self.window.resizable(False, False)
        # Chamada do método "mainloop", do objeto "window".
        self.window.mainloop()