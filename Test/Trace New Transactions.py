# Importação do módulo "sys".
import sys
# Adição da pasta "Data" ao caminho do sistema.
sys.path.insert(0, '../Data')
# Importação do módulo "Geth".
import Geth
# Importação do módulo "MySQL".
import MySQL
# Importação do módulo "Contract".
import Contract
# Importação do módulo "web3".
from web3 import Web3
# Importação do módulo "random".
from random import randint
# Importação do módulo "random".
from random import sample
# A variável "geth" recebe uma instância da classe "Geth".
geth = Geth.Geth()
# A variável "mysql" recebe uma instância da classe "MySQL".
mysql = MySQL.MySQL()
# A variável "geth" recebe uma instância da classe "Contract".
contract = Contract.Contract()
# A variável "web3" recebe uma instância de "Web3.py".
web3 = Web3(Web3.HTTPProvider(geth.url))
# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser consultado.
file = open('../CSV/Contracts/0x0a5f807d7b0526f0b619c507c3e3741c75ab26b1.csv')
# A variável "abi", da classe "contract", recebe o texto contido em "file".
contract.abi = file.readline()
# A referência contida em "file" é descartada.
file.close()
# A variável "abi", da classe "contract", recebe o "ABI" do contrato.
contract.abi = contract.abi[contract.abi.index('","ABI":"') + 9 : contract.abi.index('","ContractName":"')].replace('\\', '')
# A variável "instance", da classe "contract", recebe uma intância do objeto "contract".
contract.instance = web3.eth.contract(address = Web3.toChecksumAddress('0x0a5f807d7b0526f0b619c507c3e3741c75ab26b1'), abi = contract.abi)
# A variável contadora é inicializada.
counter = 0
# Enquanto o valor de "counter" for menor do que o tamanho de "contract.instance.functions._functions", o script executará o escopo abaixo.
while counter < len(contract.instance.functions._functions):
    # Caso o tamanho de "contract.instance.functions._functions[counter]['inputs']" seja igual a zero, o script executará o escopo abaixo.
    if len(contract.instance.functions._functions[counter]['inputs']) == 0:
        print(contract.instance.encodeABI(fn_name = contract.instance.functions._functions[counter]['name']))
    # Caso o tamanho de "contract.instance.functions._functions[counter]['inputs']" seja diferente de zero, o script executará o escopo abaixo.
    else:
        # A lista "inputs" é inicializada.
        inputs = []
        # A variável contadora é inicializada.
        sub_counter = 0
        # Enquanto o valor de "sub_counter" for menor do que o tamanho de "contract.functions._functions[counter]['inputs']", o script executará o escopo abaixo.
        while sub_counter < len(contract.instance.functions._functions[counter]['inputs']):
            #
            if contract.instance.functions._functions[counter]['inputs'][sub_counter]['type'] == 'uint256':
                # A lista "inputs" é atualizada.
                inputs.append(randint(0, 2 ** sample([8, 16, 32, 64, 128, 256], 1)[0] - 1))
            else:
                # A lista "inputs" é atualizada.
                inputs.append(contract.instance.functions._functions[counter]['inputs'][sub_counter]['type'])
            # A variável contadora é incrementada.
            sub_counter += 1
        #
        print(contract.instance.functions._functions[counter]['name'], inputs)
    # A variável contadora é incrementada.
    counter += 1
# print(contract.encodeABI(fn_name = 'approve', args = [Web3.toChecksumAddress('0x2fa5a79bb3606b26db51896ec98ae898a5ae15b5'), 10]))