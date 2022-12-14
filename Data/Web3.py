# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:00:51 2022

@author: Danilo Cabral
"""
# Definição da classe "Web3".
class Web3:
    # Definição do método construtor.
    def __init__(self, url = ''):
        # Inicialização do atributo "instance".
        self.instance = Web3(Web3.HTTPProvider(url))
        