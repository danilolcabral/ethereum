# Importação do módulo "sys".
import sys
# Adição da pasta "App" ao caminho do sistema.
sys.path.insert(0, '../Data')
# Importação do módulo "Geth".
import Geth
# A variável "geth" recebe uma instância da classe "Geth".
geth = Geth.Geth()
# A variável "trace" recebe o retorno do método "transactions_by_block()", da classe "geth".
trace = geth.non_legacy_trace_call('0xdd21d4ddf6af83fdc8efc0d59508451299c8d79c', '0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f', 400000, '0x34DA411E00', '0x34DA411E00', 2300000000000000700, '0x7ff36ab50000000000000000000000000000000000000000000000398d04f396da5c0000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000013307b8854a95946b54a904100afd0767a7a577b0000000000000000000000000000000000000000000000000000000061b668d30000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc200000000000000000000000092d6c1e31e14520e676a687f0a93788b716beff5', '0x1', [], '0x658', 13792689, '0x61B66421', '0x2950F7A7FF70D4', '0x1AF2A823B6')
# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
file = open('../CSV/Test/Non-Legacy Trace Call.csv', 'w')
# A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
file.write(str(trace))
# A referência contida em "file" é descartada.
file.close()
# Impressão para melhor visualização dos dados.
print('Done!')