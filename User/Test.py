# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:22:10 2022

@author: Danilo Cabral
"""
# Importação do módulo "tkinter".
from tkinter import Tk
# Importação do módulo "Form".
import Form
# A variável "window" recebe uma instância da classe "Tk".
window = Tk()
# A variável "form" recebe uma instância da classe "Form".
form = Form.Form(window)
# Chamada do método "trace_transaction()", do objeto "form".
form.trace_transaction()
# Chamada do método "title()", do objeto "window".
window.title('Ethereum\'s Gas Cost Predictor ')
# Chamada do método "geometry()", do objeto "window".
window.geometry("1000x600+10+10")
# Chamada do método "iconbitmap()", do objeto "window".
window.iconbitmap('../images/ethereum.ico')
# Chamada do método "resizable()", do objeto "window".
window.resizable(False, False)
# Chamada do método "mainloop", do objeto "window".
window.mainloop()