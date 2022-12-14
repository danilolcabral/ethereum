# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:52:29 2022

@author: Danilo Cabral.
"""
# Definição da classe "Etherscan".
class Etherscan:
    # Definição do método construtor.
    def __init__(self, api_key = '4YH3EQINIIG62PR7VGASU9PFH1TSTCGGD8'):
        # Inicialização do atributo "apy_key".
        self.api_key = api_key
    # Definição do método "transactions_by_contract()".
    def transactions_by_contract(self, contract, start, end, offset):
        # Importação do módulo "requests".
        import requests
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.get()".   
            response = requests.get('https://api.etherscan.io/api?module=account' \
                                    + '&action=txlist' \
                                    + '&address=' + contract \
                                    + '&startblock=' + str(start) \
                                    + '&endblock=' + str(end)\
                                    + '&page=1' \
                                    + '&offset=' + str(offset) \
                                    + '&sort=desc' \
                                    + '&apikey=' + '4YH3EQINIIG62PR7VGASU9PFH1TSTCGGD8')
            # A variável "text" recebe o valor de "response.text" sanitizado.
            text = response.text[40 : -3]
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = text.split('},{')
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "transactions_by_block()".
    def transactions_by_block(self, block):
        # Importação do módulo "requests".
        import requests
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.get()". 
            response = requests.get('https://api.etherscan.io/api?module=proxy' \
                                    + '&action=eth_getBlockByNumber' \
                                    + '&tag=' + hex(block) \
                                    + '&boolean=true' \
                                    + '&apikey=' + self.api_key)
            # A variável "text" recebe as transações contidas em "response".
            text = response.text[response.text.index('"transactions"') + 17 : response.text.index('}],"transactionsRoot"')]
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = text.split('},{')
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output  
    # Definição do método "last_block".
    def last_block(self):
        # Importação do módulo "requests".
        import requests
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.get()". 
            response = requests.get('https://api.etherscan.io/api?module=proxy' \
                                    + '&action=eth_blockNumber' \
                                    + '&apikey=' + self.api_key)
            # Número do bloco mais recente.
            block = response.text[response.text.index('0x'):-3]
            # O dicionário "output" é atualizado na posição "last_block".
            output['last_block'] = int(block, 16)
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "last_block".
            output['last_block'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "contract_abi".
    def contract_abi(self, contract):
        # Importação do módulo "requests".
        import requests
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.get()". 
            response = requests.get('https://api.etherscan.io/api?module=contract' \
                                    + '&action=getabi' \
                                    + '&address=' + contract \
                                    + '&apikey=' + self.api_key)
            # O dicionário "output" é atualizado na posição "contract_abi".
            output['contract_abi'] = response.text
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "contract_abi".
            output['contract_abi'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "contract_source".
    def contract_source(self, contract):
        # Importação do módulo "requests".
        import requests
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.get()". 
            response = requests.get('https://api.etherscan.io/api?module=contract' \
                                    + '&action=getsourcecode' \
                                    + '&address=' + contract \
                                    + '&apikey=' + self.api_key)
            # O dicionário "output" é atualizado na posição "contract_source".
            output['contract_source'] = response.text
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "contract_source".
            output['contract_source'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output 