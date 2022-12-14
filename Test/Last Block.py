# Importação do módulo "sys".
import sys
# Adição da pasta "App" ao caminho do sistema.
sys.path.insert(0, '../Data')
# Importação do módulo "Geth".
import Geth
# A variável "geth" recebe uma instância da classe "Geth".
geth = Geth.Geth()
# A variável "response" recebe o retorno do método "last_block()", da classe "geth".
response = geth.last_block()
# Impressão para melhor visualização dos dados.
print(response['last_block'])