# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import json

pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Ouro Preto',
    'enderecos': [
        {'rua 1': 'R1', 'numero': 32},
        {'rua 2': 'R2', 'numero': 55},
                  ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula42.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

with open('aula42.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    #print(pessoa)
    #print(type(pessoa))
    print(pessoa['nome'])