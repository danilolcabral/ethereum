import requests
import json

url = "http://10.0.1.2:8545"

payload = json.dumps({
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": [
    hex(13804879),
    True
  ],
  "id": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
file = open('../CSV/Test/Block by Number.csv', 'w')
# A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
file.write(response.text)
# A referência contida em "file" é descartada.
file.close()

print('Done!')