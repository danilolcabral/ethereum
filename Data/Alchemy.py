# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:11:42 2022

@author: Danilo Cabral.
"""
# Definição da classe "Alchemy".
class Alchemy:
    # Definição do método construtor.
    def __init__(self, api_key = 'flx4QuzGkkxO-i4V8TnqykkstyNq0J4j'):
        # Inicialização do atributo "apy_key".
        self.api_key = api_key
    # Definição do método "estimate_gas()".
    def estimate_gas(self, data, contract, value, block):
        # Importação do módulo "web3".
        from web3 import Web3
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "web3" recebe uma instância de "Web3.py".
            web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + self.api_key))
            # O dicionário "output" é atualizado na posição "estimate_gas".
            output['estimate_gas'] = web3.eth.estimate_gas({'data' : data, 'to':contract, 'value': value}, hex(int(block)))
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "estimate_gas".
            output['estimate_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "number_of_transactions()".
    def number_of_transactions(self, contract):
        # Importação do módulo "web3".
        from web3 import Web3
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "web3" recebe uma instância de "Web3.py".
            web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/' + self.api_key))
            # O dicionário "output" é atualizado na posição "number_of_transactions".
            output['number_of_transactions'] = web3.eth.get_transaction_count(Web3.toChecksumAddress(contract))
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "number_of_transactions".
            output['number_of_transactions'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output