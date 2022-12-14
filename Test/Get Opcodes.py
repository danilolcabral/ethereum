# Importação do módulo "sys".
import sys
# Adição da pasta "App" ao caminho do sistema.
sys.path.insert(0, '../App')
# Importação do módulo "Application".
import Application
# A variável "application" recebe uma instância da classe "Application".
application = Application.Application()
# Execução do método "trace_first_transactions()", da classe "application".
application.get_opcodes('Trace Transaction.csv', 'Test.txt')