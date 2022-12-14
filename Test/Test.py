import requests
import json

url = "http://10.0.1.2:8545"

payload = json.dumps({
  "jsonrpc": "2.0",
  "method": "debug_traceCall",
  "params": [
    {
      "from": "0xdd21d4ddf6af83fdc8efc0d59508451299c8d79c",
      "to": "0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f",
      "gas": "0x61A80",
      "maxFeePerGas": "0x34DA411E00",
      "maxPriorityFeePerGas": "0x34DA411E00",
      "value": "0x1FEB3DD0676602BC",
      "input": "0x7ff36ab50000000000000000000000000000000000000000000000398d04f396da5c0000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000013307b8854a95946b54a904100afd0767a7a577b0000000000000000000000000000000000000000000000000000000061b668d30000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc200000000000000000000000092d6c1e31e14520e676a687f0a93788b716beff5",
      "chainId": "0x1",
      "accessList": [],
      "nonce": "0x658"
    },
    "0xD275B0",
    {
      "disableStorage": True,
      "disableMemory": True,
      "blockoverrides": {
        "number": "0xD275B1",
        "time": "0x61B66421",
        "difficulty": "0x2950F7A7FF70D4",
        "baseFee": "0x1AF2A823B6"
      }
    }
  ],
  "id": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# A variável "file" recebe o retorno da função "open()", referenciando o arquivo a ser criado/alterado.
file = open('../CSV/Test/Non-Legacy Trace Call.csv', 'w')
# A função "write" escreve o conteúdo de "response.text" no arquivo referenciado por "file".
file.write(response.text)
# A referência contida em "file" é descartada.
file.close()

print('Done!')
