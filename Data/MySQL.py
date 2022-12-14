# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:56:12 2022

@author: Danilo Cabral.
"""
# Definição da classe "MySQL".
class MySQL:
    # Definição do método construtor.
    def __init__(self, my_host = 'localhost', my_user = 'root', my_password = '', my_database = 'ethereum'):
        # Importação do módulo "mysql.connector".
        import mysql.connector
        # A variável "database" recebe uma nova instância do banco de dados passado como parâmetro.
        self.database = mysql.connector.connect(host = my_host, user = my_user, password = my_password, database = my_database)
        # A variável "cursor" recebe o retorno do método "cursor()", pertencente ao objeto "database".
        self.cursor = self.database.cursor()
    # Definição do método "insert_block()".
    def insert_block(self, block_number, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'INSERT INTO `block`(`block_number`, `block_hash`, `block_time`, `block_difficulty`, `block_base_fee`, `block_gas_limit`, `block_miner`, `block_random`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        # A variável "values" recebe os dados a serem inseridos no banco de dados.
        values = (block_number, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql, values)
            # Execução do método "commit()", do objeto "database".
            self.database.commit()
            # Retorno do método.
            return 'Block {} successfully inserted.'.format(str(block_number))
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Block {} not inserted.'.format(str(block_number))
    # Definição do método "insert_contract()".
    def insert_contract(self, address, block_number):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'INSERT INTO `contract`(`address`, `block_number`) VALUES (%s, %s)'
        # A variável "values" recebe os dados a serem inseridos no banco de dados.
        values = (address, block_number)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql, values)
            # Execução do método "commit()", do objeto "database".
            self.database.commit()
            # Retorno do método.
            return 'Contract {} successfully inserted.'.format(str(address))
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Contract {} not inserted.'.format(str(address))
    # Definição do método "insert_legacy_transaction()".
    def insert_legacy_transaction(self, transaction_hash, transaction_index, transaction_mode, transaction_type, from_address, to_address, nonce, value, data, gas_limit, used_gas, transaction_status, trace_gas, trace_status, estimate_gas, block_number):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'INSERT INTO `transaction`(`hash`, `transaction_index`, `transaction_mode`, `transaction_type`, `from_address`, `to_address`, `nonce`, `value`, `data`, `gas_limit`, `used_gas`, `transaction_status`, `trace_gas`, `trace_status`, `estimate_gas`, `block_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # A variável "values" recebe os dados a serem inseridos no banco de dados.
        values = (transaction_hash, transaction_index, transaction_mode, transaction_type, from_address, to_address, nonce, value, data, gas_limit, used_gas, transaction_status, trace_gas, trace_status, estimate_gas, block_number)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql, values)
            # Execução do método "commit()", do objeto "database".
            self.database.commit()
            # Retorno do método.
            return 'Transaction {} successfully inserted.'.format(str(transaction_hash))
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Transaction {} not inserted.'.format(str(transaction_hash))
    # Definição do método "insert_non_legacy_transaction()".
    def insert_non_legacy_transaction(self, transaction_hash, transaction_index, transaction_mode, transaction_type, from_address, to_address, nonce, value, data, chain_id, access_list, max_fee_per_gas, max_priority_fee_per_gas, gas_limit, used_gas, transaction_status, trace_gas, trace_status, estimate_gas, block_number):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'INSERT INTO `transaction`(`hash`, `transaction_index`, `transaction_mode`, `transaction_type`, `from_address`, `to_address`, `nonce`, `value`, `data`, `chain_id`, `access_list`, `max_fee_per_gas`, `max_priority_fee_per_gas`, `gas_limit`, `used_gas`, `transaction_status`, `trace_gas`, `trace_status`, `estimate_gas`, `block_number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # A variável "values" recebe os dados a serem inseridos no banco de dados.
        values = (transaction_hash, transaction_index, transaction_mode, transaction_type, from_address, to_address, nonce, value, data, chain_id, access_list, max_fee_per_gas, max_priority_fee_per_gas, gas_limit, used_gas, transaction_status, trace_gas, trace_status, estimate_gas, block_number)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql, values)
            # Execução do método "commit()", do objeto "database".
            self.database.commit()
            # Retorno do método.
            return 'Transaction {} successfully inserted.'.format(str(transaction_hash))
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Transaction {} not inserted.'.format(str(transaction_hash))
    # Definição do método "insert_trace()".
    def insert_trace(self, creation_block_number, trace_transaction_hash, created_contract_address, trace_block, trace_block_delta, trace_gas, trace_status, trace_error, trace_delta):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'INSERT INTO `trace`(`creation_block_number`, `trace_transaction_hash`, `created_contract_address`, `trace_block`, `trace_block_delta`, `trace_gas`, `trace_status`, `trace_error`, `trace_delta`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # A variável "values" recebe os dados a serem inseridos no banco de dados.
        values = (creation_block_number, trace_transaction_hash, created_contract_address, trace_block, trace_block_delta, trace_gas, trace_status, trace_error, trace_delta)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql, values)
            # Execução do método "commit()", do objeto "database".
            self.database.commit()
            # Retorno do método.
            return 'Trace transaction {} in block {} successfully performed.'.format(trace_transaction_hash, trace_block)
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 'Trace transaction {} in block {} not performed.'.format(trace_transaction_hash, trace_block)
    # Definição do método "list_transactions_by_trace_gas()".
    def list_transactions_by_trace_gas(self):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'SELECT `hash` FROM `transaction` WHERE `transaction_type` = "first" AND `used_gas` != `trace_gas`'
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql)
            # Retorno do método.
            return self.cursor.fetchall()
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return None
    # Definição do método "list_transactions_by_transaction_type()".
    def list_transactions_by_transaction_type(self):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'SELECT `to_address` FROM `transaction` WHERE `transaction_type` = "create"'
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql)
            # Retorno do método.
            return self.cursor.fetchall()
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return None
    # Definição do método "list_transactions_by_transaction_type()".
    def list_contracts_by_block(self, block_number):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'SELECT `address` FROM `contract` WHERE `block_number` > "{}"'.format(block_number)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql)
            # Retorno do método.
            return self.cursor.fetchall()
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return None
    # Definição do método "select_contract_creation_block".
    def select_contract_creation_block(self, address):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'SELECT `block_number` FROM `transaction` WHERE `to_address` = "{}" AND `transaction_type` = "create"'.format(address)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql)
            # Retorno do método.
            return self.cursor.fetchone()
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return None
    # Definição do método "list_traces_by_trace_block_delta()".
    def list_traces_by_trace_block_delta(self, trace_block_delta):
        # A variável "sql" recebe o código para a inserção dos dados no banco de dados.
        sql = 'SELECT `trace_delta` FROM `trace` WHERE `trace_block_delta` = "{}"'.format(trace_block_delta)
        # O script tentará executar o escopo abaixo.
        try:
            # Execução do método "execute()", do objeto "cursor".
            self.cursor.execute(sql)
            # Retorno do método.
            return self.cursor.fetchall()
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return None