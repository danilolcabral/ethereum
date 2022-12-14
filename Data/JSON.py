# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:56:57 2022

@author: Danilo Cabral.
"""
# Definição da classe "JSON".
class JSON:
    # Definição do método "insert_block()".
    def insert_block(self, block_number, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random):
        # A variável "text" é inicializada.
        text = '{"block_number": "' + str(block_number) + '", "block_hash": "' + str(block_hash) + '", "block_time": "' + str(block_time) + '", "block_difficulty": "' + str(block_difficulty) + '", "block_base_fee": "' + str(block_base_fee) + '", "block_gas_limit": "' + str(block_gas_limit) + '", "block_miner": "' + str(block_miner) + '", "block_random": "' + str(block_random) + '"}\n'
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser alterado.
            file = open('../JSON/Blocks.csv', 'a')
            # A função "write" escreve o cabeçalho do arquivo referenciado por "target".
            file.write(text)
            # A referência contida em "file" é descartada.
            file.close()
            # Retorno do método.
            return 'Block {} successfully inserted.'.format(str(block_number))
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Block {} not inserted.'.format(str(block_number))