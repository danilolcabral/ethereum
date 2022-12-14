# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:18:30 2022

@author: Danilo Cabral
"""
# Definição da classe "Application".
class Application:
    # Definição do método "get_contracts_abis()".
    def get_contracts_abis(self):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "MySQL".
        import MySQL
        # Importação do módulo "Etherscan".
        import Etherscan
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "transactions" recebe o retorno do método "list_transactions_by_transaction_type()", da classe "mysql".
        transactions = mysql.list_transactions_by_transaction_type()
        # Laço responsável por iterar sobre os elementos contidos em "transactions".
        for transaction in transactions:
            # A variável "contract" é atualizada
            contract = transaction[0]
            # A variável "geth" recebe uma instância da classe "Geth".
            etherscan = Etherscan.Etherscan()
            # A variável "contract_abi" recebe o retorno do método "contract_abi()", da classe "etherscan".
            contract_abi = etherscan.contract_abi(contract)
            # O script tentará executar o escopo abaixo.
            try:
                # A variável "contract_abi" é atualizada.
                contract_abi['contract_abi'] = contract_abi['contract_abi'][contract_abi['contract_abi'].index('"result":"[') + 11 : ]
                # A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
                file = open('../CSV/ABI/' + contract + '.csv', 'w')
                # A função "write" escreve a lista de transações no arquivo referenciado por "file".
                file.write(contract_abi['contract_abi'])
                # A referência contida em "file" é descartada.
                file.close()
                # Impressão para a melhor visualização dos dados.
                print('Contract ' + contract + ' was successfully registered.')
            # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
            except:
                # O script passa pela instrução sem executar nada.
                pass
    # Definição do método "get_contracts_sources()".
    def get_contracts_sources(self):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "MySQL".
        import MySQL
        # Importação do módulo "Etherscan".
        import Etherscan
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "transactions" recebe o retorno do método "list_transactions_by_transaction_type()", da classe "mysql".
        transactions = mysql.list_transactions_by_transaction_type()
        # Laço responsável por iterar sobre os elementos contidos em "transactions".
        for transaction in transactions:
            # A variável "contract" é atualizada
            contract = transaction[0]
            # A variável "geth" recebe uma instância da classe "Geth".
            etherscan = Etherscan.Etherscan()
            # A variável "contract_source" recebe o retorno do método "contract_source()", da classe "etherscan".
            contract_source = etherscan.contract_source(contract)
            # O script tentará executar o escopo abaixo.
            try:
                # A variável "contract_source" é atualizada.
                contract_source['contract_source'] = contract_source['contract_source'][contract_source['contract_source'].index('"SourceCode":""') + 15 : ]
                # O script passa pela instrução sem executar nada.
                pass
            # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
            except:
                # A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
                file = open('../CSV/Contracts/' + contract + '.csv', 'w')
                # A função "write" escreve a lista de transações no arquivo referenciado por "file".
                file.write(contract_source['contract_source'])
                # A referência contida em "file" é descartada.
                file.close()
                # Impressão para a melhor visualização dos dados.
                print('Contract ' + contract + ' was successfully registered.')
    # Definição do método "predict_transaction()".
    def get_last_block(self):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "Geth".
        import Geth
        # A variável "geth" recebe uma instância da classe "Geth".
        geth = Geth.Geth()
        # A variável "last_block" recebe o retorno do método "last_block()", da classe "geth".
        last_block = geth.last_block()
        # Impressão para melhor visualização dos dados.
        print(last_block)
        # Retorno do método.
        return last_block
    # Definição do método "trace_transactions()".
    def trace_transactions(self, decrement, delta, maximum, mode):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "json".
        import json
        # Importação do módulo "Geth".
        import Geth
        # Importação do módulo "MySQL".
        import MySQL
        # Importação do módulo "JSON".
        import JSON
        # A variável "geth" recebe uma instância da classe "Geth".
        geth = Geth.Geth()
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "js" recebe uma instância da classe "JSON".
        js = JSON.JSON()
        # A variável "last_block" recebe o retorno do método "last_block()", da classe "geth".
        last_block = geth.last_block()
        # Caso o valor de "maximum" seja igual a "0", o script executará o escopo abaixo.
        if maximum != 0:
            # A variável contadora é inicializada.
            counter = maximum
        # Caso o valor de "maximum" seja diferente de "0", o script executará o escopo abaixo.
        else:
            # A variável "last_block" recebe o retorno do método "last_block()", da classe "geth".
            last_block = geth.last_block()
            # Caso o valor de "last_block", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
            if last_block['failed'] == False:
                # A variável contadora é atualizada.
                maximum = int(last_block['last_block'])
            # Caso o valor de "last_block", na posição "failed", seja diferente de "False", o script executará o escopo abaixo.
            else:
                # A variável contadora é inicializada.
                counter = maximum
        # Laço responsável por iterar sobre os blocos da blockchain.
        while counter >= maximum - delta:
            # A variável "block" recebe o valor de "last_block".
            block = str(counter)
            # Impressão para melhor visualização dos dados.
            print('------------------------- \nBlock ' + block)
            # A variável contadora é decrementada.
            counter -= decrement
            # O script tentará executar o escopo abaixo.
            try:
                # A variável "transactions" recebe o retorno do método "transactions_by_block()", da classe "geth".
                transactions = geth.transactions_by_block(block)
                # Caso o valor de "transactions", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                if transactions['failed'] == False:
                    # A variável "block_hash" recebe o hash do bloco.
                    block_hash = transactions['block_hash']
                    # A variável "block_time" recebe o timestamp do bloco.
                    block_time = transactions['block_time']
                    # A variável "block_difficulty" recebe a dificuldade do bloco.
                    block_difficulty = transactions['block_difficulty']
                    # A variável "block_base_fee" recebe a taxa base do bloco.
                    block_base_fee = transactions['block_base_fee']
                    # A variável "block_gas_limit" recebe o limite de gás do bloco.
                    block_gas_limit = transactions['block_gas_limit']
                    # A variável "block_miner" recebe o endereço do minerador do bloco.
                    block_miner = transactions['block_miner']
                    # A variável "block_random" recebe o endereço randômico do bloco.
                    block_random = transactions['block_random']
                    # Caso o valor de "mode" seja igual a "first", o script executará o escopo abaixo.
                    if mode == 'first':
                        # A variável "first_transaction" recebe a primeira transação contida em "transactions".
                        first_transaction = transactions['transactions'][0]
                        # A variável "to_address" recebe o endereço do contrato chamado pela transação.
                        to_address = first_transaction[first_transaction.index('"to":"') + 6 : first_transaction.index('","transactionIndex":"')]
                        # A variável "transaction_hash" recebe o hash da transação.
                        transaction_hash = first_transaction[first_transaction.index('"hash":"') + 8 : first_transaction.index('","input":"')]
                        # A variável "transaction_hash" recebe o hash da transação.
                        transaction_index = first_transaction[first_transaction.index('"transactionIndex":"') + 20 : first_transaction.index('","value":"')]
                        # A variável "transaction_index" é convertida para a notação decimal.
                        transaction_index = str(int(transaction_index, 16))
                        # A variável "from_address" recebe o endereço invocador da transação.
                        from_address = first_transaction[first_transaction.index('"from":"') + 8 : first_transaction.index('","gas":"')]
                        # A variável "value" recebe o valor enviado juntamente com a transação.
                        value = first_transaction[first_transaction.index('"value":"') + 9 : first_transaction.index('","type":"')]
                        # A variável "value" é convertida para a notação decimal.
                        value = str(int(value, 16))
                        # A variável "gas_limit" recebe o limite do gas a ser utilizado pela transação.
                        gas_limit = first_transaction[first_transaction.index('"gas":"') + 7 : first_transaction.index('","gasPrice":"')]
                        # A variável "gas_limit" é convertida para a notação decimal.
                        gas_limit = str(int(gas_limit, 16))
                        # A variável "data" recebe os dados de entrada da transação.
                        data = first_transaction[first_transaction.index('"input":"') + 9 : first_transaction.index('","nonce":"')]
                        # O script tentará executar o escopo abaixo.
                        try:
                            # A variável "type_transaction" recebe o tipo da transação.
                            type_transaction = first_transaction[first_transaction.index('"type":"') + 8 : first_transaction.index('","accessList":')]
                        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
                        except:
                            # A variável "type_transaction" recebe o tipo da transação.
                            type_transaction = first_transaction[first_transaction.index('"type":"') + 8 : first_transaction.index('","v":')]
                        # A variável "type_transaction" é convertida para a notação decimal.
                        type_transaction = str(int(type_transaction, 16))
                        # A variável "transaction_receipt" recebe o retorno do método "transaction_receipt()", da classe "geth".
                        transaction_receipt = geth.transaction_receipt(transaction_hash)
                        # Caso o valor de "transaction_receipt", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                        if transaction_receipt['failed'] == False:
                            # Caso a transação não seja apenas de pagamento entre contas, o script executará o escopo abaixo.
                            if transaction_receipt['used_gas'] != '21000' or data != '0x':
                                # Caso o valor de "type_transaction" seja igual a "0", o script executará o escopo abaixo.
                                if type_transaction == '0':
                                    # A variável "trace_gas" recebe o retorno do método "legacy_trace_call()", da classe "geth".
                                    trace_gas = geth.legacy_trace_call(from_address, to_address, gas_limit, value, data, block, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random)
                                # Caso o valor de "type_transaction" diferente de "0", o script executará o escopo abaixo.
                                else:
                                    # A variável "max_fee_per_gas" recebe a taxa máxima da transação.
                                    max_fee_per_gas = first_transaction[first_transaction.index('"maxFeePerGas":"') + 16 : first_transaction.index('","maxPriorityFeePerGas":"')]
                                    # A variável "max_priority_fee_per_gas" recebe a prioridade da taxa máxima da transação.
                                    max_priority_fee_per_gas = first_transaction[first_transaction.index('"maxPriorityFeePerGas":"') + 24 : first_transaction.index('","hash":"')]
                                    # A variável "chain_id" recebe o id do canal da transação.
                                    chain_id = first_transaction[first_transaction.index('"chainId":"') + 11 : first_transaction.index('","v":"')]
                                    # A variável "access_list" recebe a lista de acesso da transação.
                                    access_list = first_transaction[first_transaction.index('"accessList":') + 13 : first_transaction.index(',"chainId":"')]
                                    # A variável "access_list_string" recebe o valor de "access_list".
                                    access_list_string = access_list
                                    # A variável "access_list" é atualizada.
                                    access_list = access_list[2 : -2].split('},{')
                                    # Definição do contador "access_counter".
                                    access_counter = 0
                                    # Enquanto o valor de "access_counter" for menor do que o tamanho de "access_list", o script executará o escopo abaixo.
                                    while access_counter < len(access_list):
                                        # O conteúdo de "access_list[access_counter]" é transformado em dicionário.
                                        access_list[access_counter] = json.loads('{' + access_list[access_counter] + '}')
                                        # O contador "access_counter" é incrementado.
                                        access_counter += 1
                                    # Se o conteúdo de "access_list_string" representar uma lista vazia, o script executará o escopo abaixo.
                                    if access_list_string == '[]':
                                        # A lista "access_list" é limpa.
                                        access_list.clear()
                                    # A variável "nonce" recebe o nonce da transação.
                                    nonce = first_transaction[first_transaction.index('"nonce":"') + 9 : first_transaction.index('","to":')] 
                                    # A variável "trace_gas" recebe o retorno do método "non_legacy_trace_call()", da classe "geth".
                                    trace_gas = geth.non_legacy_trace_call(from_address, to_address, gas_limit, max_fee_per_gas, max_priority_fee_per_gas, value, data, chain_id, access_list, nonce, block, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random)
                                # Caso o valor de "trace_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                if trace_gas['failed'] == False:
                                    # Caso o valor de "type_transaction" seja igual a "0", o script executará o escopo abaixo.
                                    if type_transaction == '0':
                                        # A variável "estimate_gas" recebe o retorno do método "legacy_estimate_gas()", da classe "geth".
                                        estimate_gas = geth.legacy_estimate_gas(from_address, to_address, gas_limit, value, data, block)
                                        # Caso o valor de "estimate_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                        if estimate_gas['failed'] == False:
                                            # A variável "estimate_gas['estimated_gas']" é convertida para a notação decimal.
                                            estimate_gas['estimate_gas'] = str(int(estimate_gas['estimate_gas'], 16))
                                            # Impressão da execução do método "insert_block()", pertencente à classe "mysql".
                                            print(mysql.insert_block(block, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random))
                                            # Impressão da execução do método "insert_block()", pertencente à classe "js".
                                            print(js.insert_block(block, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random))
                                            # Impressão da execução do método "insert_contract()", pertencente à classe "mysql".
                                            print(mysql.insert_contract(to_address, block))
                                            # Impressão da execução do método "insert_legacy_transaction()", pertencente à classe "mysql".
                                            print(mysql.insert_legacy_transaction(transaction_hash, transaction_index,'first', type_transaction, from_address, to_address, nonce, value, data, gas_limit, transaction_receipt['used_gas'], transaction_receipt['status'], trace_gas['trace_gas'], trace_gas['status'], estimate_gas['estimate_gas'], block))
                                    # Caso o valor de "type_transaction" diferente de "0", o script executará o escopo abaixo.
                                    else:
                                        # A variável "estimate_gas" recebe o retorno do método "non_legacy_estimate_gas()", da classe "geth".
                                        estimate_gas = geth.non_legacy_estimate_gas(from_address, to_address, gas_limit, max_fee_per_gas, max_priority_fee_per_gas, value, data, chain_id, access_list, nonce, block)
                                        # Caso o valor de "estimate_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                        if estimate_gas['failed'] == False:
                                            # A variável "estimate_gas['estimated_gas']" é convertida para a notação decimal.
                                            estimate_gas['estimate_gas'] = str(int(estimate_gas['estimate_gas'], 16))
                                            # Impressão da execução do método "insert_block()", pertencente à classe "mysql".
                                            print(mysql.insert_block(block, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random))
                                            # Impressão da execução do método "insert_block()", pertencente à classe "js".
                                            print(js.insert_block(block, block_hash, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random))
                                            # Impressão da execução do método "insert_contract()", pertencente à classe "mysql".
                                            print(mysql.insert_contract(to_address, block))
                                            # Impressão da execução do método "insert_legacy_transaction()", pertencente à classe "mysql".
                                            print(mysql.insert_non_legacy_transaction(transaction_hash, transaction_index,'first', type_transaction, from_address, to_address, nonce, value, data, chain_id, str(access_list), max_fee_per_gas, max_priority_fee_per_gas, gas_limit, transaction_receipt['used_gas'], transaction_receipt['status'], trace_gas['trace_gas'], trace_gas['status'], estimate_gas['estimate_gas'], block))
                    # Caso o valor de "mode" seja igual a "create", o script executará o escopo abaixo.
                    elif mode == 'create':
                        pass
            # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
            except:
                # O script termina a execução sem nenhuma impressão.
                pass
    # Definição do método "trace_all_transactions()".
    def trace_all_transactions(self, block_delta, block_decrement, trace_delta, trace_decrement):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "Geth".
        import Geth
        # Importação do módulo "MySQL".
        import MySQL
        # A variável "geth" recebe uma instância da classe "Geth".
        geth = Geth.Geth()
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "last_block" recebe o retorno do método "last_block()", da classe "geth".
        last_block = geth.last_block()
        # Caso o valor de "last_block", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
        if last_block['failed'] == False:
            # A variável contadora é inicializada.
            counter = int(last_block['last_block'])
            # Laço responsável por iterar sobre os blocos da blockchain.
            while counter >= int(last_block['last_block']) - block_delta:
                # A variável "block" recebe o valor de "last_block".
                block = str(counter)
                # Impressão para melhor visualização dos dados.
                print('------------------------- \nBlock ' + block)
                # A variável contadora é decrementada.
                counter -= block_decrement
                # O script tentará executar o escopo abaixo.
                try:
                    # A variável "transactions" recebe o retorno do método "transactions_by_block()", da classe "geth".
                    transactions = geth.transactions_by_block(block)
                    # Caso o valor de "transactions", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                    if transactions['failed'] == False:
                        # Laço responsável por iterar sobre cada uma das transações contidas em "transactions['transactions']".
                        for transaction in transactions['transactions']:
                            # A variável "to_address" recebe o endereço do contrato chamado pela transação.
                            to_address = transaction[transaction.index('"to":') + 5 : transaction.index(',"transactionIndex":"')]
                            # Caso o valor de "to_address" seja diferente de "null", o script executará o escopo abaixo.
                            if to_address != 'null':
                                # A variável "block_hash" recebe o hash do bloco da transação.
                                block_hash = transaction[transaction.index('"blockHash":"') + 13 : transaction.index('","blockNumber":"')]
                                # A variável "to_address" é atualizada.
                                to_address = to_address.replace('"', '')
                                # A variável "transaction_hash" recebe o hash da transação.
                                transaction_hash = transaction[transaction.index('"hash":"') + 8 : transaction.index('","input":"')]                        
                                # A variável "create_block" recebe o retorno do método "select_contract_creation_block()", da classe "mysql".
                                create_block = mysql.select_contract_creation_block(to_address)
                                # Caso o retorno de "create_block" seja diferente de "None", o script executará o escopo abaixo.
                                if (create_block != None):
                                    # A variável "transaction_hash" recebe o hash da transação.
                                    transaction_index = transaction[transaction.index('"transactionIndex":"') + 20 : transaction.index('","value":"')]
                                    # A variável "transaction_index" é convertida para a notação decimal.
                                    transaction_index = str(int(transaction_index, 16))
                                    # A variável "from_address" recebe o endereço invocador da transação.
                                    from_address = transaction[transaction.index('"from":"') + 8 : transaction.index('","gas":"')]
                                    # A variável "value" recebe o valor enviado juntamente com a transação.
                                    value = transaction[transaction.index('"value":"') + 9 : transaction.index('","type":"')]
                                    # A variável "value" é convertida para a notação decimal.
                                    value = str(int(value, 16))
                                    # A variável "gas_limit" recebe o limite do gas a ser utilizado pela transação.
                                    gas_limit = transaction[transaction.index('"gas":"') + 7 : transaction.index('","gasPrice":"')]
                                    # A variável "gas_limit" é convertida para a notação decimal.
                                    gas_limit = str(int(gas_limit, 16))
                                    # A variável "transaction_receipt" recebe o retorno do método "transaction_receipt()", da classe "geth".
                                    transaction_receipt = geth.transaction_receipt(transaction_hash)
                                    # Caso o valor de "transaction_receipt", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                    if transaction_receipt['failed'] == False:
                                        # A variável "data" recebe os dados de entrada da transação.
                                        data = transaction[transaction.index('"input":"') + 9 : transaction.index('","nonce":"')]
                                        # Caso a transação não seja apenas de pagamento entre contas, o script executará o escopo abaixo.
                                        if transaction_receipt['used_gas'] != '21000' or data != '0x':
                                            # A variável "trace_gas" recebe o retorno do método "predicted_gas()", da classe "geth".
                                            trace_gas = geth.trace_call(from_address, to_address, gas_limit, value, data, block)
                                            # Caso o valor de "trace_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                            if trace_gas['failed'] == False:
                                                # A variável "estimate_gas" recebe o retorno do método "estimated_gas()", da classe "geth".
                                                estimate_gas = geth.estimate_gas(from_address, to_address, gas_limit, value, data, block)
                                                # Caso o valor de "estimate_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                                if estimate_gas['failed'] == False:
                                                    # A variável "estimate_gas['estimated_gas']" é convertida para a notação decimal.
                                                    estimate_gas['estimate_gas'] = str(int(estimate_gas['estimate_gas'], 16))
                                                    # Impressão da execução do método "insert_block()", pertencente à classe "mysql".
                                                    print(mysql.insert_block(block, block_hash))
                                                    # Impressão da execução do método "insert_contract()", pertencente à classe "mysql".
                                                    print(mysql.insert_contract(to_address, block))
                                                    # Impressão da execução do método "insert_trace_transaction()", pertencente à classe "mysql".
                                                    print(mysql.insert_trace_transaction(transaction_hash, transaction_index, from_address, to_address, value, data, gas_limit, transaction_receipt['used_gas'], transaction_receipt['status'], trace_gas['trace_gas'], trace_gas['status'], estimate_gas['estimate_gas'], block))
                                                    # A variável contadora é inicializada.
                                                    sub_counter = int(block)
                                                    # A variável "real_trace_gas" é inicializada.
                                                    real_trace_gas = trace_gas['trace_gas']
                                                    # Laço responsável por iterar sobre os blocos da blockchain.
                                                    while sub_counter >= int(block) - trace_delta:   
                                                        # A variável "trace_gas" recebe o retorno do método "predicted_gas()", da classe "geth".
                                                        trace_gas = geth.trace_call(from_address, to_address, gas_limit, value, data, str(sub_counter))
                                                        # Caso o valor de "trace_gas", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                                                        if trace_gas['failed'] == False:
                                                            # Impressão da execução do método "insert_trace()", pertencente à classe "mysql".
                                                            print(mysql.insert_trace(create_block[0], transaction_hash, to_address, sub_counter, int(block) - sub_counter, trace_gas['trace_gas'], trace_gas['status'], int(trace_gas['trace_gas']) - int(transaction_receipt['used_gas']), int(trace_gas['trace_gas']) - int(real_trace_gas)))
                                                        # A variável contadora é decrementada.
                                                        sub_counter -= trace_decrement
                # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
                except:
                    # O script termina a execução sem nenhuma impressão.
                    pass
    # Definição do método "compare_traces_with_transactions()".
    def compare_traces_with_transactions(self, start_block, end_block):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "os".
        import os
        # Importação do módulo "Geth".
        import Geth
        # Importação do módulo "MySQL".
        import MySQL
        # String contendo a primeira parte do caminho até o diretório atual.
        parent = os.getcwd()
        # A variável "geth" recebe uma instância da classe "Geth".
        geth = Geth.Geth()
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "transactions" recebe o retorno do método "list_transactions_by_trace_gas()", da classe "mysql".
        transactions = mysql.list_transactions_by_trace_gas()
        # Laço responsável por iterar sobre os elementos contidos em "transactions".
        for transaction in transactions:
            # String contendo a última parte do caminho até o diretório atual.
            directory = 'CSV/Transactions/' + transaction[0]
            # String contendo o caminho completo até o diretório atual.
            path = os.path.join(parent[0 : -4], directory)
            # O script tentará executar o escopo abaixo.
            try:
                # O script criará o diretório referenciado por "path".
                os.mkdir(path)
                # Impressão do texto informando que o diretório foi criado com sucesso.
                print(transaction[0] + ' folder successfully created. \n')
            # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
            except FileExistsError:
                # Impressão do texto informando que o diretório já existe.
                print(transaction[0] + ' folder already exists. \n')
            # String contendo a última parte do caminho até o diretório atual.
            directory = 'CSV/Transactions/' + transaction[0] + '/Transaction'
            # String contendo o caminho completo até o diretório atual.
            path = os.path.join(parent[0 : -4], directory)
            # O script tentará executar o escopo abaixo.
            try:
                # O script criará o diretório referenciado por "path".
                os.mkdir(path)
                # Impressão do texto informando que o diretório foi criado com sucesso.
                print('Transaction in ' + transaction[0] + ' folder successfully created. \n')
            # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
            except FileExistsError:
                # Impressão do texto informando que o diretório já existe.
                print('Transaction in ' + transaction[0] + ' folder already exists. \n')
            # A variável "trace_transaction" recebe o retorno do método "trace_transaction()", da classe "geth".
            trace_transaction = geth.trace_transaction(transaction[0])
            # Caso o valor de "trace_transaction", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
            if trace_transaction['failed'] == False:
                # A variável "transaction_file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
                transaction_file = open('../CSV/Transactions/' + transaction[0] + '/Transaction/' + transaction[0] + '.csv', 'w')
                # A função "write" escreve o conteúdo de "trace_transaction" no arquivo referenciado por "transaction_file".
                transaction_file.write(trace_transaction[trace_transaction])
                # A referência contida em "transaction_file" é descartada.
                transaction_file.close()
                # A variável contadora é inicializada.
                counter = start_block
                # Laço responsável por iterar sobre os blocos da blockchain.
                while counter <= end_block:
                    # String contendo a última parte do caminho até o diretório atual.
                    directory = 'CSV/Transactions/' + transaction[0] + '/Trace Block -' + str(counter)
                    # String contendo o caminho completo até o diretório atual.
                    path = os.path.join(parent[0 : -4], directory)
                    # O script tentará executar o escopo abaixo.
                    try:
                        # O script criará o diretório referenciado por "path".
                        os.mkdir(path)
                        # Impressão do texto informando que o diretório foi criado com sucesso.
                        print(transaction[0] + ' - Trace Block -' + str(counter) + ' folder successfully created. \n')
                    # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
                    except FileExistsError:
                        # Impressão do texto informando que o diretório já existe.
                        print(transaction[0] + ' - Trace Block -' + str(counter) + ' folder already exists. \n')
                    # A variável "trace_call" recebe o retorno do método "full_trace_call()", da classe "geth".
                    trace_call = geth.full_trace_call(transaction[2], transaction[3], transaction[6], transaction[4], transaction[5], int(transaction[12]) - counter)
                    # Caso o valor de "trace_call", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
                    if trace_call['failed'] == False:
                        # A variável "call_file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
                        call_file = open('../CSV/Transactions/' + transaction[0] + '/Trace Block -' + str(counter) + '/' + transaction[0] + '.csv', 'w')
                        # A função "write" escreve o conteúdo de "trace_call" no arquivo referenciado por "call_file".
                        call_file.write(trace_call['trace_call'])
                        # A referência contida em "call_file" é descartada.
                        call_file.close()
                    # A variável contadora é incrementada.
                    counter += 1
                # Impressão para a melhor visualização dos dados.
                print('Transaction ' + transaction[0] + ' was successfully registered.\n')
            # Caso o valor de "transactions", na posição "failed", seja igual a "False", o script executará o escopo abaixo.
            else:
                # Impressão para a melhor visualização dos dados.
                print('Transaction ' + transaction[0] + ' wasn\'t registered.\n')
    # Definição do método "predict_with_built_in_gas_cost_predictor()".
    def predict_with_built_in_gas_cost_predictor(self, from_address, to_address, gas_limit, value, data, block):
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "MySQL".
        import MySQL
        # Importação do módulo "Geth".
        import Geth
        # Importação do módulo "statistics".
        import statistics
        # A variável "mysql" recebe uma instância da classe "MySQL".
        mysql = MySQL.MySQL()
        # A variável "geth" recebe uma instância da classe "Geth".
        geth = Geth.Geth()
        # A variável "delta_block" é inicializada.
        delta_block = 0
        # A variável "delta_tuples" recebe o retorno do método "list_traces_by_trace_block_delta()", da classe "mysql".
        delta_tuples = mysql.list_traces_by_trace_block_delta(delta_block)
        # A variável "delta_block" é incrementada.
        delta_block += 1
        # A variável "delta_numbers" recebe os valores de "delta_tuples" convertidos em inteiros.
        delta_numbers = list(int(item[0]) for item in delta_tuples)
        # A variável "delta" recebe a mediana de "delta_numbers".
        delta = float(statistics.median(delta_numbers))
        # A variável "trace_gas" recebe o retorno do método "predicted_gas()", da classe "geth".
        # trace_gas = geth.trace_call(from_address, to_address, gas_limit, value, data, block)
        # A variável "trace_gas" é incrementada com o valor de "delta".
        # trace_gas += delta
        # Retorno do método.
        return delta
    # Definição do método "predict_with_recent_gas_usage_model()".
    def predict_with_recent_gas_usage_model(self, contract, start_block, end_block, offset, number_of_results, function_name):
        # Importação do módulo "statistics".
        from statistics import mean
        # Importação do módulo "sys".
        import sys
        # Adição da pasta "Data" ao caminho do sistema.
        sys.path.insert(0, '../Data')
        # Importação do módulo "Etherscan".
        import Etherscan
        # A variável "geth" recebe uma instância da classe "Geth".
        etherscan = Etherscan.Etherscan()
        # A variável "transactions" recebe o retorno do método "transactions_by_contract()", da classe "etherscan".
        transactions = etherscan.transactions_by_contract(contract, start_block, end_block, offset)
        # A variável gas é inicializada.
        gas = []
        # Laço responsável por iterar sobre os elementos contidos em "transactions".
        for transaction in transactions['transactions']:
            # A variável "function" é inicializada.
            input_name = transaction[transaction.index('"input":"') + 9 : transaction.index('"input":"') + 19]
            # Caso o valor de "function" seja igual ao de "function", o script executará o escopo abaixo.
            if input_name == function_name and len(gas) < number_of_results:
                # A variável "gas" é atualizada.
                gas.append(int(transaction[transaction.index('"gasUsed":"') + 11 : transaction.index('","confirmations":"')]))
        # O script tentará executar o escopo abaixo.
        try:
            # Retorno do método.
            return mean(gas)
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # Retorno do método.
            return 0

    # Definição do método "get_opcodes()".
    def get_opcodes(self, source, target):
        # A variável "trace" recebe o retorno da função "open()", referenciando o arquivo a ser consultado.
        trace = open('../CSV/Opcodes/' + source)
        # A variável "transaction" é atualizada.
        transaction = trace.readline()
        # A referência contida em "trace" é descartada.
        trace.close()
        # O dicionário "opcodes" é inicializado.
        opcodes = {}
        # Enquanto houver "'"op":"'" em "transaction", o script executará o escopo abaixo.
        while '"op":"' in transaction:
            # A variável "op" é inicializada.
            op = transaction[transaction.index('"op":"') + 6: transaction.index('","gas"')]
            # Impressão para melhor visualização dos dados.
            if op in opcodes:  # Caso exista o valor de "op" em "opcodes", o script executará o script abaixo.
                # A variável "opcode" é atualizada.
                opcodes.update({op: opcodes[op] + 1})
            else:  # Caso não exista o valor de "op" em "opcodes", o script executará o script abaixo.
                # A variável "opcodes" é atualizada.
                opcodes[op] = 1
            # A variável "transaction" é atualizada.
            transaction = transaction[transaction.index('","gas"') + 7:]
        # O dicionário "opcodes" é ordenado.
        opcodes = dict(sorted(opcodes.items()))
        # A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
        file = open('../CSV/Opcodes/' + target, 'w')
        # A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
        file.write(str(opcodes))
        # A referência contida em "file" é descartada.
        file.close()
        # Impressão para melhor visualização.
        print('Done!')

    # Definição do método "compare_opcodes()".
    def compare_opcodes(self, first, second):
        # Importação do módulo "ast".
        import ast
        # A variável "first_file" recebe o retorno da função "open()", referenciando o arquivo a ser consultado.
        first_file = open('../CSV/Opcodes/' + first)
        # A variável "first_dictionary" é atualizada.
        first_dictionary = ast.literal_eval(first_file.readline())
        # A referência contida em "first_file" é descartada.
        first_file.close()
        # A variável "second_file" recebe o retorno da função "open()", referenciando o arquivo a ser consultado.
        second_file = open('../CSV/Opcodes/' + second)
        # A variável "second_dictionary" é atualizada.
        second_dictionary = ast.literal_eval(second_file.readline())
        # A referência contida em "second_file" é descartada.
        second_file.close()
        # A variável "different_keys" é inicializada.
        different_keys = [k for k in first_dictionary if first_dictionary[k] != second_dictionary[k]]
        # Laço responsável por identificar os elementos diferentes entre "first_dictionary" e "second_dictionary".
        for k in different_keys:
            # Impressão para melhor visualização dos dados.
            print(k, ':', first_dictionary[k], '->', second_dictionary[k])