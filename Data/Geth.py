# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:47:56 2022

@author: Danilo Cabral.
"""
# Definição da classe "Geth".
class Geth:
    # Definição do método construtor.
    def __init__(self, url = 'http://10.0.1.2:8545'):
        # Inicialização do atributo "url".
        self.url = url
    # Definição do método "last_block()".
    def last_block(self):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          "jsonrpc": "2.0",
          "method": "eth_blockNumber",
          "params": [],
          "id": 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # A variável "block" recebe o número do último block da blockchain.
            block = response.text[response.text.index('"result":"') + 10 : - 3]
            # A variável "block" é convertida para um valor inteiro.
            block = int(block, 16)
            # O dicionário "output" é atualizado na posição "last_block".
            output['last_block'] = str(block)
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
    # Definição do método "transaction_count()".
    def transaction_count(self, transaction_hash):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          "jsonrpc": "2.0",
          "method": "eth_getTransactionCount",
          "params": [
            transaction_hash,
            "latest"
          ],
          "id": 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "transaction_count".
            output['transaction_count'] = response.text
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "transaction_count".
            output['transaction_count'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "block_hash()".
    def block_hash(self, block):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_getBlockByNumber',
          'params': [
            hex(int(block)),
            True
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "block_hash".
            output['block_hash'] = response.text[response.text.index('"blockHash":"') + 13 : response.text.index('","blockNumber":')]
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "block_hash".
            output['block_hash'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "transactions_by_block()".
    def transactions_by_block(self, block):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_getBlockByNumber',
          'params': [
            hex(int(block)),
            True
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "block_hash".
            output['block_hash'] = response.text[response.text.index('"blockHash":"') + 13 : response.text.index('","blockNumber":')]
            # O dicionário "output" é atualizado na posição "block_time".
            output['block_time'] = response.text[response.text.index('"timestamp":"') + 13 : response.text.index('","totalDifficulty":')]
            # O dicionário "output" é atualizado na posição "block_difficulty".
            output['block_difficulty'] = response.text[response.text.index('"difficulty":"') + 14 : response.text.index('","extraData":')]
            # O dicionário "output" é atualizado na posição "block_base_fee".
            output['block_base_fee'] = response.text[response.text.index('"baseFeePerGas":"') + 17 : response.text.index('","difficulty":')]
            # O dicionário "output" é atualizado na posição "block_gas_limit".
            output['block_gas_limit'] = response.text[response.text.index('"gasLimit":"') + 12 : response.text.index('","gasUsed":')]
            # O dicionário "output" é atualizado na posição "block_miner".
            output['block_miner'] = response.text[response.text.index('"miner":"') + 9 : response.text.index('","mixHash":')]
            # O dicionário "output" é atualizado na posição "block_random".
            output['block_random'] = response.text[response.text.index('"parentHash":"') + 14 : response.text.index('","receiptsRoot":')]
            # Texto para inserção no arquivo.
            text = response.text[response.text.index('"transactions":[{') + 17 : response.text.index('}],"transactionsRoot"')]
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = text.split('"},{')
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "block_hash".
            output['block_hash'] = ''
            # O dicionário "output" é atualizado na posição "block_time".
            output['block_time'] = ''
            # O dicionário "output" é atualizado na posição "block_difficulty".
            output['block_difficulty'] = ''
            # O dicionário "output" é atualizado na posição "block_base_fee".
            output['block_base_fee'] = ''
            # O dicionário "output" é atualizado na posição "block_gas_limit".
            output['block_gas_limit'] = ''
            # O dicionário "output" é atualizado na posição "block_miner".
            output['block_miner'] = ''
            # O dicionário "output" é atualizado na posição "block_random".
            output['block_random'] = ''
            # O dicionário "output" é atualizado na posição "transactions".
            output['transactions'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "transaction_receipt()".
    def transaction_receipt(self, transaction_hash):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_getTransactionReceipt',
          'params': [transaction_hash],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # A variável "status" recebe o status da transação.
            status = response.text[response.text.index('"status":"') + 10 : response.text.index('","to":')]
            # A variável "status" é convertida para um valor inteiro.
            status = int(status, 16)
            # A variável "used_gas" recebe o gas utilizado pela transação.
            used_gas = response.text[response.text.index('"gasUsed":"') + 11 : response.text.index('","logs":')]
            # A variável "used_gas" é convertida para um valor inteiro.
            used_gas = int(used_gas, 16)
            # O dicionário "output" é atualizado na posição "status".
            output['status'] = str(status)
            # O dicionário "output" é atualizado na posição "used_gas".
            output['used_gas'] = str(used_gas)
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "status".
            output['status'] = ''
            # O dicionário "output" é atualizado na posição "used_gas".
            output['used_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "legacy_trace_call()".
    def legacy_trace_call(self, from_address, to_address, gas_limit, value, data, block_number, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'debug_traceCall',
          'params': [
            {
              'from': from_address,
              'to': to_address,
              'gas': hex(int(gas_limit)),
              'value': hex(int(value)),
              'data': data
            },
            hex(int(block_number) - 1),
            {
              'disableStorage': False,
              'disableStack': False,
              'enableMemory': True,
              'enableReturnData': True,
              'blockoverrides': {
                'number': hex(int(block_number)),
                'time': block_time,
                'difficulty': block_difficulty,
                'baseFee': block_base_fee,
                'gasLimit': block_gas_limit,
                'coinbase': block_miner,
                'random': block_random
              }
            }
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['status'] =  response.text[response.text.index('"failed":') + 9 : response.text.index(',"returnValue":')]
            # Caso o valor de "output", na posição "status", seja igual a "false", o script executará o escopo abaixo.
            if output['status'] == 'false':
                # O dicionário "output" é atualizado na posição "status".
                output['status'] = 1
            # Caso o valor de "output", na posição "status", seja diferente de "false", o script executará o escopo abaixo.
            else:
                # O dicionário "output" é atualizado na posição "status".
                output['status'] = 0
            # Caso a transação tenha consumido gas, o script executará o escopo abaixo.
            if '{"gas":' in response.text:
                # O dicionário "output" é atualizado na posição "trace_gas".
                output['trace_gas'] =  response.text[response.text.index('{"gas":') + 7 : response.text.index(',"failed":')]
            # Caso a transação não tenha consumido gas, o script executará o escopo abaixo.
            else:
                # O dicionário "output" é atualizado na posição "trace_gas".
                output['trace_gas'] = '0'
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "status".
            output['status'] == ''
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['trace_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "non_legacy_trace_call()".
    def non_legacy_trace_call(self, from_address, to_address, gas_limit, max_fee_per_gas, max_priority_fee_per_gas, value, data, chain_id, access_list, nonce, block_number, block_time, block_difficulty, block_base_fee, block_gas_limit, block_miner, block_random):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'debug_traceCall',
          'params': [
            {
              'from': from_address,
              'to': to_address,
              'gas': hex(int(gas_limit)),
              'maxFeePerGas': max_fee_per_gas,
              'maxPriorityFeePerGas': max_priority_fee_per_gas,
              'value': hex(int(value)),
              'input': data,
              'chainId': chain_id,
              'accessList': access_list,
              'nonce': nonce
            },
            hex(int(block_number) - 1),
            {
              'disableStorage': False,
              'disableStack': False,
              'enableMemory': True,
              'enableReturnData': True,
              'blockoverrides': {
                'number': hex(int(block_number)),
                'time': block_time,
                'difficulty': block_difficulty,
                'baseFee': block_base_fee,
                'gasLimit': block_gas_limit,
                'coinbase': block_miner,
                'random': block_random
              }
            }
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['status'] =  response.text[response.text.index('"failed":') + 9 : response.text.index(',"returnValue":')]
            # Caso o valor de "output", na posição "status", seja igual a "false", o script executará o escopo abaixo.
            if output['status'] == 'false':
                # O dicionário "output" é atualizado na posição "status".
                output['status'] = 1
            # Caso o valor de "output", na posição "status", seja diferente de "false", o script executará o escopo abaixo.
            else:
                # O dicionário "output" é atualizado na posição "status".
                output['status'] = 0
            # Caso a transação tenha consumido gas, o script executará o escopo abaixo.
            if '{"gas":' in response.text:
                # O dicionário "output" é atualizado na posição "trace_gas".
                output['trace_gas'] =  response.text[response.text.index('{"gas":') + 7 : response.text.index(',"failed":')]
            # Caso a transação não tenha consumido gas, o script executará o escopo abaixo.
            else:
                # O dicionário "output" é atualizado na posição "trace_gas".
                output['trace_gas'] = '0'
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "status".
            output['status'] == ''
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['trace_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "legacy_estimate_gas()".
    def legacy_estimate_gas(self, from_address, to_address, gas_limit, value, data, block):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_estimateGas',
          'params': [
            {
              'from': from_address,
              'to': to_address,
              'gas': hex(int(gas_limit)),
              'value': hex(int(value)),
              'data': data
            },
            hex(int(block) - 1)
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "estimate_gas".
            output['estimate_gas'] = response.text[response.text.index('"result":"') + 10 : response.text.index('"}\n')]
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
    # Definição do método "non_legacy_estimate_gas()".
    def non_legacy_estimate_gas(self, from_address, to_address, gas_limit, max_fee_per_gas, max_priority_fee_per_gas, value, data, chain_id, access_list, nonce, block):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_estimateGas',
          'params': [
            {
              'from': from_address,
              'to': to_address,
              'gas': hex(int(gas_limit)),
              'maxFeePerGas': max_fee_per_gas,
              'maxPriorityFeePerGas': max_priority_fee_per_gas,
              'value': hex(int(value)),
              'input': data,
              'chainId': chain_id,
              'accessList': access_list,
              'nonce': nonce
            },
            hex(int(block) - 1)
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "estimate_gas".
            output['estimate_gas'] = response.text[response.text.index('"result":"') + 10 : response.text.index('"}\n')]
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
    # Definição do método "trace_transaction()".
    def trace_transaction(self, transaction_hash):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'debug_traceTransaction',
          'params': [
            transaction_hash,
            {}
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "trace_transaction".
            output['trace_transaction'] = response.text
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "trace_transaction".
            output['trace_transaction'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "full_trace_call()".
    def full_trace_call(self, from_address, to_address, gas_limit, value, data, block):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'debug_traceCall',
          'params': [
            {
              'from': from_address,
              'to': to_address,
              'gas': hex(int(gas_limit)),
              'value': hex(int(value)),
              'data': data
            },
            hex(int(block) - 1),
            {
              'disableStorage': False,
              'disableStack': False,
              'enableMemory': True,
              'enableReturnData': True
            }
          ],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['trace_gas'] = response.text
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "trace_gas".
            output['trace_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output
    # Definição do método "full_transaction_receipt()".
    def full_transaction_receipt(self, transaction_hash):
        # Importação do módulo "requests".
        import requests
        # Importação do módulo "json".
        import json
        # A variável "payload" recebe os dados da transação.
        payload = json.dumps({
          'jsonrpc': '2.0',
          'method': 'eth_getTransactionReceipt',
          'params': [transaction_hash],
          'id': 1
        })
        # A variável "headers" recebe o cabeçalho da transação.
        headers = {
          'Content-Type' : 'application/json'
        }
        # Definição do dicionário "output".
        output = {}
        # O script tentará executar o escopo abaixo.
        try:
            # A variável "response" recebe o retorno da função "requests.request()". 
            response = requests.request('POST', self.url, headers = headers, data = payload)
            # A variável "status" recebe o status da transação.
            status = response.text[response.text.index('"status":"') + 10 : response.text.index('","to":')]
            # A variável "status" é convertida para um valor inteiro.
            status = int(status, 16)
            # A variável "used_gas" recebe o gas utilizado pela transação.
            used_gas = response.text[response.text.index('"gasUsed":"') + 11 : response.text.index('","logs":')]
            # A variável "used_gas" é convertida para um valor inteiro.
            used_gas = int(used_gas, 16)
            # O dicionário "output" é atualizado na posição "used_gas".
            output['transaction'] = response.text
            # O dicionário "output" é atualizado na posição "status".
            output['status'] = str(status)
            # O dicionário "output" é atualizado na posição "used_gas".
            output['used_gas'] = str(used_gas)
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = False
        # Caso o bloco "try" não seja executado, o script executará o escopo abaixo.
        except:
            # O dicionário "output" é atualizado na posição "transaction".
            output['transaction'] = ''
            # O dicionário "output" é atualizado na posição "status".
            output['status'] = ''
            # O dicionário "output" é atualizado na posição "used_gas".
            output['used_gas'] = ''
            # O dicionário "output" é atualizado na posição "failed".
            output['failed'] = True
        # Retorno do método.
        return output