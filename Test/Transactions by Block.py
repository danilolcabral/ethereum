# Importação do módulo "sys".
import sys
# Adição da pasta "App" ao caminho do sistema.
sys.path.insert(0, '../Data')
# Importação do módulo "Geth".
import Geth
# A variável "geth" recebe uma instância da classe "Geth".
geth = Geth.Geth()
# A variável "transactions" recebe o retorno do método "transactions_by_block()", da classe "geth".
transactions = geth.transactions_by_block(13804879)
# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
file = open('../CSV/Test/Transactions by Block.csv', 'w')
# A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
file.write(str(transactions))
# A referência contida em "file" é descartada.
file.close()
# Impressão para melhor visualização dos dados.
print('Done!')