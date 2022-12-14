# Importação do módulo "sys".
import sys
# Adição da pasta "App" ao caminho do sistema.
sys.path.insert(0, '../App')
# Importação do módulo "Application".
import Application
# A variável "application" recebe uma instância da classe "Application".
application = Application.Application()
# Execução do método "trace_transactions()", da classe "application".
application.trace_transactions(1, 20, 13788647, "first")
# application.trace_transactions(1, 0, 13798526, "first")