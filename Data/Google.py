# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:15:48 2022

@author: Danilo Cabral
"""
# Definição da classe "Google".
class Google:
    # Definição do método "big_query()".
    def big_query(self, sql, path):
        # Importação do módulo "bigquery".
        from google.cloud import bigquery
        # A variável "client" recebe uma instância de "Client" em "bigquery.py".
        client = bigquery.Client()
        # A variável "query" recebe o retorno do método "query()" do objeto "client".
        query = client.query(sql)
        # A variável "rows_iterable" recebe o retorno do método "result()" do objeto "query".
        rows_iterable = query.result()
        # A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
        file = open(path, 'w')
        # Laço responsável por iterar sobre cada uma das linhas contidas em "rows_iterable".
        for row in rows_iterable:
            # A variável "text" recebe o valor de "row".
            text = str(row) + '\n'
            # A função "write" escreve a lista de transações no arquivo referenciado por "file".
            file.write(text)
        # A referência contida em "file" é descartada.
        file.close()