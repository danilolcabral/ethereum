# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:56:08 2022

@author: Danilo Cabral
"""
# Definição da classe "Contract".
class Contract:
    # Definição do método construtor.
    def __init__(self, address = '', abi = '', instance = ''):
        # Inicialização do atributo "address".
        self.address = address
        # Inicialização do atributo "abi".
        self.abi = abi
        # Inicialização do atributo "instance".
        self.instance = instance