import requests
import json

url = "http://10.0.1.2:8545"

payload = json.dumps({
  "jsonrpc": "2.0",
  "method": "debug_traceTransaction",
  "params": [
    "0xc5de8aec593f973cc2bf129915b6e48f1c06d78ede60e0ec905b610fb0a7145e"
  ],
  "id": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
file = open('../CSV/Test/Trace Transaction.csv', 'w')
# A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
file.write(response.text)
# A referência contida em "file" é descartada.
file.close()

print('Done!')
